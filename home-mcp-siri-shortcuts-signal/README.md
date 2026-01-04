🇰🇷 [한국어 README 보기](README.ko.md)

# HomeMCP Signal (iOS Shortcut)

**HomeMCP Signal** is a voice interface layer that connects
natural language voice commands from **iOS Siri Shortcuts**
to executable **HomeMCP server control requests (URLs)**.

This repository focuses on **iOS Shortcut distribution and user configuration**
within the HomeMCP ecosystem.

---

## What does this repository provide?

- Distribution of the iOS shortcut `Signal.shortcut`
- Canonical LLM prompt definitions (LLM #1 / LLM #2)
- Installation and configuration guides for end users

---

## Position in the overall HomeMCP architecture

```
[User Voice]
      ↓
[iOS Siri / Signal Shortcut]
      ↓
[LLM #1] Natural Language → Control URL
      ↓
[HomeMCP Core Server]
      ↓
[IoT / Device / Agent]
      ↓
[LLM #2] Response Summary → User
```

The Signal shortcut acts as the **entry point that bridges Siri and the HomeMCP Core server**.

---

## Quick Start (Summary)

1. Install the iOS shortcut  
   - `install/iCloud-link.md`

2. Rename the shortcut (recommended)  
   - The shortcut name is used directly as the Siri invocation phrase.

3. Configure LLM prompts  
   - Copy and paste the LLM #1 and LLM #2 prompts into the shortcut.

4. Test with voice commands  
   - Example: “Turn on the living room light”

For detailed, step-by-step instructions, see:

👉 **install/setup-checklist.md**

---

## LLM Prompt Architecture

The Signal shortcut uses a **two-stage LLM pipeline**.

### LLM #1 – URL Generator
- Converts user voice or text input
- Into a single executable **HomeMCP Control URL**

### LLM #2 – Response Summarizer
- Converts HomeMCP server responses (JSON)
- Into a **single, natural sentence** spoken back to the user

Prompt file locations:

- `prompts/llm1_url_generator/v1.md`
- `prompts/llm2_response_summarizer/v1.en.md`

---

## About the Shortcut Name (Important)

On iOS, the **shortcut name itself becomes the Siri invocation phrase**.

The default name is `Signal`, but users are encouraged to rename it
to any phrase that feels natural for voice interaction.

Detailed renaming instructions are included in the setup guide.

---
