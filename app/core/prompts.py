"""
Gemini prompts for SEO brief generation
"""

SEO_BRIEF_PROMPT = """You are an expert SEO content strategist with years of experience creating high-ranking content. Generate a comprehensive SEO brief for the following content:

**Title:** {title}
**Target Audience:** {target_audience}
**Primary Keywords:** {primary_keywords}
**Secondary Keywords:** {secondary_keywords}

Create a detailed SEO brief that will help a content writer create optimized content. Your response must be valid JSON with this exact structure:

{{
    "meta_title": "A compelling meta title under 60 characters that includes the primary keyword",
    "meta_description": "A compelling meta description under 155 characters that encourages clicks and includes keywords",
    "h1_suggestion": "The main H1 heading for the page",
    "content_outline": [
        "Introduction section description",
        "Main section 1 with key points to cover",
        "Main section 2 with key points to cover",
        "Main section 3 with key points to cover",
        "Conclusion section description"
    ],
    "word_count_recommendation": 1500,
    "keyword_placement_tips": [
        "Specific tip for keyword placement 1",
        "Specific tip for keyword placement 2",
        "Specific tip for keyword placement 3"
    ],
    "internal_linking_suggestions": [
        "Suggested internal link topic 1",
        "Suggested internal link topic 2",
        "Suggested internal link topic 3"
    ]
}}

Important guidelines:
- Make the meta title compelling and under 60 characters
- Make the meta description action-oriented and under 155 characters
- Provide 4-6 detailed content outline sections
- Recommend appropriate word count based on topic complexity
- Give specific, actionable keyword placement tips
- Suggest relevant internal linking opportunities

Respond ONLY with valid JSON. Do not include any markdown formatting, code blocks, or explanations.
"""
