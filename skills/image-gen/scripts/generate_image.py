#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
# ]
# ///
"""
Marketing Playbook Image Generator

Generate marketing images using Google's Gemini API (Nano Banana Pro).
Optimized for OpenGraph images, social media graphics, and web banners.

Requires GEMINI_API_KEY environment variable.

Usage:
    uv run scripts/generate_image.py "Your prompt" --type og
    uv run scripts/generate_image.py "Your prompt" --output ./path/to/image.jpg
    uv run scripts/generate_image.py "Edit this image" --input ./photo.jpg

Note: Images are saved to ./generated/ by default to keep root clean.

Marketing presets:
    og          - OpenGraph / Facebook / LinkedIn (1200x630, ~1.91:1)
    twitter     - Twitter Card large (16:9)
    instagram   - Instagram square (1:1)
    story       - Instagram/TikTok story (9:16)
    linkedin    - LinkedIn post (4:3)
    banner      - Web banner wide (16:9)
    article     - Article header (16:9)
    portrait    - Portrait format (3:4)
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image


# Marketing image presets with aspect ratios
# Note: Gemini supports these ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
IMAGE_PRESETS = {
    "og": {
        "aspect": "16:9",  # Closest to 1.91:1 (1200x630)
        "name": "OpenGraph / Facebook / LinkedIn",
        "description": "Social sharing preview cards",
    },
    "twitter": {
        "aspect": "16:9",
        "name": "Twitter Card",
        "description": "Twitter large image card",
    },
    "instagram": {
        "aspect": "1:1",
        "name": "Instagram Square",
        "description": "Instagram feed post",
    },
    "story": {
        "aspect": "9:16",
        "name": "Instagram/TikTok Story",
        "description": "Vertical story format",
    },
    "linkedin": {
        "aspect": "4:3",
        "name": "LinkedIn Post",
        "description": "LinkedIn feed image",
    },
    "banner": {
        "aspect": "16:9",
        "name": "Web Banner",
        "description": "Website hero/banner",
    },
    "ultrawide": {
        "aspect": "21:9",
        "name": "Ultra-wide Banner",
        "description": "Cinematic website header",
    },
    "article": {
        "aspect": "16:9",
        "name": "Article Header",
        "description": "Blog/article featured image",
    },
    "portrait": {
        "aspect": "3:4",
        "name": "Portrait",
        "description": "Vertical portrait format",
    },
    "pinterest": {
        "aspect": "2:3",
        "name": "Pinterest",
        "description": "Pinterest optimal pin",
    },
}

# Valid aspect ratios supported by Gemini
VALID_ASPECTS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]

# Valid resolutions
VALID_RESOLUTIONS = ["1K", "2K", "4K"]


def load_env_file() -> None:
    """Load environment variables from .env.local if it exists."""
    env_file = Path(".env.local")
    if not env_file.exists():
        env_file = Path(__file__).parent.parent / ".env.local"

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())


def get_api_key(api_key_arg: str | None = None) -> str:
    """Get API key from argument, .env.local, or environment variable."""
    if api_key_arg:
        return api_key_arg

    # Try to load from .env.local first
    load_env_file()

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("Error: GEMINI_API_KEY not found.", file=sys.stderr)
        print("\nSet it in .env.local:", file=sys.stderr)
        print('  GEMINI_API_KEY=your-api-key-here', file=sys.stderr)
        print("\nOr export it:", file=sys.stderr)
        print('  export GEMINI_API_KEY="your-api-key-here"', file=sys.stderr)
        sys.exit(1)

    return key


def generate_filename(prompt: str, image_type: str | None = None) -> str:
    """Generate a timestamped filename in the generated/ directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create short descriptive name from prompt
    words = prompt.lower().split()[:3]
    name_part = "-".join(w for w in words if w.isalnum())[:30]

    # Always use generated/ directory for auto-generated filenames
    output_dir = Path("generated")
    output_dir.mkdir(exist_ok=True)

    if image_type:
        return str(output_dir / f"{timestamp}-{image_type}-{name_part}.jpg")
    return str(output_dir / f"{timestamp}-{name_part}.jpg")


def generate_image(
    prompt: str,
    output_path: str,
    aspect_ratio: str = "16:9",
    resolution: str = "1K",
    input_image_path: str | None = None,
    api_key: str | None = None,
    model: str = "gemini-3-pro-image-preview",
) -> Path:
    """
    Generate or edit an image using Gemini API.

    Args:
        prompt: Text description or editing instructions
        output_path: Where to save the generated image
        aspect_ratio: Aspect ratio (e.g., "16:9", "1:1")
        resolution: Image resolution ("1K", "2K", "4K")
        input_image_path: Optional input image for editing
        api_key: API key (uses env var if not provided)
        model: Gemini model to use

    Returns:
        Path to the saved image
    """
    key = get_api_key(api_key)
    client = genai.Client(api_key=key)

    # Build contents - either just prompt or prompt + image for editing
    if input_image_path:
        input_image = Image.open(input_image_path)
        contents = [prompt, input_image]
        print(f"Editing image: {input_image_path}")
    else:
        contents = [prompt]

    print(f"Generating with {model}...")
    print(f"Aspect ratio: {aspect_ratio}, Resolution: {resolution}")

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=resolution,
            ),
        ),
    )

    output_file = Path(output_path)

    # Process response parts
    for part in response.parts:
        if part.text is not None:
            print(f"\nModel response: {part.text}")
        elif part.inline_data is not None:
            image = part.as_image()
            # Gemini returns JPEG by default - save with correct extension
            if not output_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                output_file = output_file.with_suffix(".jpg")
            image.save(output_file)
            print(f"\nImage saved to: {output_file}")
            return output_file

    raise RuntimeError("No image generated in response. Check your prompt and try again.")


def list_presets():
    """Print available marketing presets."""
    print("\nAvailable marketing presets:\n")
    print(f"{'Preset':<12} {'Aspect':<8} {'Name':<30} {'Description'}")
    print("-" * 80)
    for key, preset in IMAGE_PRESETS.items():
        print(f"{key:<12} {preset['aspect']:<8} {preset['name']:<30} {preset['description']}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate marketing images with Gemini API (Nano Banana Pro)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate OG image
  uv run scripts/generate_image.py "Abstract tech illustration" --type og

  # Generate with custom aspect ratio and 4K resolution
  uv run scripts/generate_image.py "Modern gradient background" --aspect 16:9 --resolution 4K

  # Edit existing image
  uv run scripts/generate_image.py "Add dramatic lighting" --input ./photo.jpg

  # List available presets
  uv run scripts/generate_image.py --list-presets
        """,
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        help="Image description or editing instructions",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: auto-generated)",
    )
    parser.add_argument(
        "--type", "-t",
        choices=IMAGE_PRESETS.keys(),
        help="Marketing preset (og, twitter, instagram, etc.)",
    )
    parser.add_argument(
        "--aspect", "-a",
        choices=VALID_ASPECTS,
        help="Custom aspect ratio (overrides --type)",
    )
    parser.add_argument(
        "--resolution", "-r",
        choices=VALID_RESOLUTIONS,
        default="1K",
        help="Image resolution: 1K (fast), 2K, 4K (best quality). Default: 1K",
    )
    parser.add_argument(
        "--input", "-i",
        dest="input_image",
        help="Input image for editing (enables edit mode)",
    )
    parser.add_argument(
        "--model", "-m",
        default="gemini-3-pro-image-preview",
        help="Gemini model (default: gemini-3-pro-image-preview)",
    )
    parser.add_argument(
        "--api-key",
        help="API key (default: uses GEMINI_API_KEY env var)",
    )
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="List available marketing presets",
    )

    args = parser.parse_args()

    # Handle list presets
    if args.list_presets:
        list_presets()
        return

    # Require prompt if not listing presets
    if not args.prompt:
        parser.error("prompt is required (or use --list-presets)")

    # Determine aspect ratio
    if args.aspect:
        aspect_ratio = args.aspect
    elif args.type:
        aspect_ratio = IMAGE_PRESETS[args.type]["aspect"]
    else:
        aspect_ratio = "16:9"  # Default to OG/banner size

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = generate_filename(args.prompt, args.type)

    # Generate image
    try:
        result = generate_image(
            prompt=args.prompt,
            output_path=output_path,
            aspect_ratio=aspect_ratio,
            resolution=args.resolution,
            input_image_path=args.input_image,
            api_key=args.api_key,
            model=args.model,
        )

        # Print summary
        print("\n" + "=" * 50)
        print("Generation complete!")
        print(f"File: {result}")
        print(f"Type: {args.type or 'custom'}")
        print(f"Aspect: {aspect_ratio}")
        print(f"Resolution: {args.resolution}")
        if args.input_image:
            print(f"Mode: Edit (based on {args.input_image})")
        print("=" * 50)

    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
