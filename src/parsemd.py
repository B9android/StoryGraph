import frontmatter

input = """
---
title: My Cats
categories: ["cats","pets"]
description: Why cats are better than dogs.
---

This is the rest of the content.
"""

data = frontmatter.loads(input)

print("Title", data["title"])
