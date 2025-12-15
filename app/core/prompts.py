"""
Gemini prompts for SEO brief generation
"""

SEO_BRIEF_PROMPT = """You are an expert SEO content strategist. Generate a complete SEO content brief for the following topic:

**Title:** {title}
**Target Audience:** {target_audience}
**Primary Keywords:** {primary_keywords}
**Secondary Keywords:** {secondary_keywords}

Create a comprehensive, ready-to-use SEO brief in plain text format. Structure it clearly with sections that a content writer can easily follow. Include:

1. **META TITLE** (under 60 characters, include primary keyword)

2. **META DESCRIPTION** (under 155 characters, compelling and action-oriented)

3. **H1 HEADING** (main page heading)

4. **RECOMMENDED WORD COUNT** (based on topic complexity)

5. **CONTENT OUTLINE**
   - Write detailed section headings with brief descriptions of what to cover
   - Include 5-8 main sections
   - Make it comprehensive and actionable

6. **KEYWORD PLACEMENT TIPS**
   - Where to place primary keywords
   - Where to place secondary keywords
   - Natural integration strategies

7. **INTERNAL LINKING SUGGESTIONS**
   - Related topics to link to
   - Anchor text recommendations

Format the response as a clean, readable document that can be easily copied and used by a content writer. Use clear headings and bullet points. Do NOT use JSON format - provide plain text only.
"""
