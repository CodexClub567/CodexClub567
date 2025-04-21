def generate_metadata(script):
    """
    Generates SEO metadata (title, description, tags) for a video script.

    Args:
        script: The video script.

    Returns:
        A dictionary containing the metadata, or None on error.
    """
    # Placeholder:  Implement SEO optimization logic.
    #  Use NLP techniques to extract keywords and create a compelling description.
    try:
        title = script[:50] + "..." if len(script) > 50 else script # create a title
        description = script[:150] + "..." if len(script) > 150 else script # create description
        tags = ["old money", "luxury", "lifestyle"]  # Example tags
        metadata = {
            "title": title,
            "description": description,
            "tags": tags,
        }
        return metadata
    except Exception as e:
        print(f"Error generating SEO metadata: {e}")
        return None
