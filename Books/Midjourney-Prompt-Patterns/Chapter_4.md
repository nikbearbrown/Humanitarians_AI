# Prompt Templates

Creating effective prompts is an art that can be greatly enhanced by using templates. This chapter explores the structure, design, and implementation of prompt templates, guiding you through basic, intermediate, and advanced templates. We also delve into using parameters for better control, dissect the anatomy of prompts, and provide exercises to help you craft custom templates.

---

## Introduction to Prompt Templates

Prompt templates are predefined structures designed to simplify the process of crafting detailed and complex prompts. They ensure consistency in your prompts and help achieve specific artistic effects more efficiently. Templates can range from basic structures for beginners to advanced patterns that professionals use to create intricate and nuanced images.

---

## Basic Prompt Templates for Beginners

Basic templates focus on essential elements like the subject, environment, and style. These templates are ideal for users just starting with Midjourney.

### Basic Template 1: Simple Subject and Environment

```plaintext
/imagine "A [subject] in [environment]"
```

**Example**:  
```plaintext
/imagine "A fox resting in a forest clearing"
```

---

### Basic Template 2: Adding Style

```plaintext
/imagine "A [subject] in [environment] in [style] style"
```

**Example**:  
```plaintext
/imagine "A portrait of a knight in a Renaissance painting style"
```

---

### Basic Template 3: Simple Actions

```plaintext
/imagine "A [subject] [action] in [environment]"
```

**Example**:  
```plaintext
/imagine "A child flying a kite in a grassy meadow"
```

---

## Intermediate Prompt Templates: Combining Elements

Intermediate templates introduce actions, specific styles, and detailed environments, creating more dynamic and visually appealing images.

### Intermediate Template 1: Action and Detail

```plaintext
/imagine "A [subject] [action] in a [detailed environment] in [style] style"
```

**Example**:  
```plaintext
/imagine "A dragon breathing fire in a stormy canyon in a dark fantasy style"
```

---

### Intermediate Template 2: Mood and Lighting

```plaintext
/imagine "A [subject] in [environment] under [lighting conditions] in [mood] mood"
```

**Example**:  
```plaintext
/imagine "A castle on a hill under moonlight in a mysterious mood"
```

---

### Intermediate Template 3: Multi-Prompt Combination

```plaintext
/imagine "[Subject and action] -- AND -- [Another subject and action] in [environment]"
```

**Example**:  
```plaintext
/imagine "A bustling market square at dawn -- AND -- a merchant arranging fruit on a stall"
```

---

## Advanced Prompt Templates: Complex Creations

Advanced templates combine multiple elements, actions, specific styles, and nuanced details. They are ideal for creating intricate scenes and professional-grade images.

### Advanced Template 1: Complex Composition

```plaintext
/imagine "A [subject] [action] in [environment] with [specific lighting], featuring [details], in [complex style] style"
```

**Example**:  
```plaintext
/imagine "An elven archer aiming at a target in a misty forest, with golden sunlight filtering through the trees, featuring intricate leaf patterns, in a hyperrealistic style"
```

---

### Advanced Template 2: Narrative Scene

```plaintext
/imagine "A [subject] [action] in [environment] with [another subject] in [specific style], [mood], [lighting]"
```

**Example**:  
```plaintext
/imagine "A pirate captain holding a treasure map in a candlelit cabin, with a parrot perched on their shoulder, in a cinematic style, adventurous mood, warm lighting"
```

---

### Advanced Template 3: Mixed Media and Artistic Influence

```plaintext
/imagine "A [subject] in [environment], [action], combining [style 1] and [style 2], inspired by [artist or art movement]"
```

**Example**:  
```plaintext
/imagine "A surreal garden with floating flowers, combining Van Gogh’s impressionism with Escher’s geometry, inspired by surrealism"
```

---

## Using Parameters in Templates for Enhanced Control

Parameters are essential for fine-tuning your prompts. They help control aspects like aspect ratio, quality, and stylization, ensuring the generated image aligns with your vision.

### Example with Parameters

```plaintext
/imagine "A [subject] in [environment] under [lighting conditions] --ar [aspect ratio] --q [quality] --stylize [stylization]"
```

**Example**:  
```plaintext
/imagine "A futuristic cityscape at night under neon lights --ar 16:9 --q 2 --stylize 80"
```

---

## Zebonastic.ai Expanded Prompt Pattern

The Zebonastic.ai pattern helps craft rich, detailed prompts for creating visually stunning images.

```plaintext
/imagine "Subject: [subject] | Medium: [medium] | Environment: [environment] | Lighting: [lighting] | Color: [color scheme] | Mood: [mood] | Composition: [composition elements] | Boosters: [specific details or parameters]"
```

**Example**:  
```plaintext
/imagine "Subject: Astronaut on a distant planet | Medium: Photorealistic | Environment: Barren alien desert | Lighting: Dusk with long shadows | Color: Warm oranges and purples | Mood: Majestic and solitary | Composition: Wide-angle shot with astronaut centered | Boosters: Ultra-high resolution, cinematic lighting --ar 16:9"
```

---

## Anatomy of Prompts

### Components of a Well-Structured Prompt

1. **Subject**: The main focus of your image.  
   *Example*: `/imagine "A majestic griffin"`

2. **Medium**: The artistic style or method.  
   *Example*: `/imagine "A watercolor painting of a castle"`

3. **Environment**: The setting or background.  
   *Example*: `/imagine "A knight in a foggy battlefield"`

4. **Lighting**: The light source and its effects.  
   *Example*: `/imagine "A sunset illuminating a forest glade"`

5. **Color**: The palette used in the image.  
   *Example*: `/imagine "A cityscape in neon blue and pink"`

6. **Mood**: The emotional tone.  
   *Example*: `/imagine "A serene lake with a calming atmosphere"`

7. **Composition**: Arrangement of elements.  
   *Example*: `/imagine "A portrait with a centered subject"`

8. **Boosters**: Additional enhancements.  
   *Example*: `/imagine "A scenic vista with ultra-high resolution --q 2"`

---

## Practice Exercise: Crafting Custom Prompts

### Step 1: Identify Key Elements
Decide on the subject, environment, mood, and style you want to use.

### Step 2: Write Your Prompt
Structure it to include all necessary components.  
*Template*:  
```plaintext
/imagine "A [subject] [action] in [environment], with [lighting], in [style], with [color scheme], focusing on [details], [mood]"
```

**Example**:  
```plaintext
/imagine "A phoenix soaring through a stormy sky, with lightning strikes in the background, in a surreal style, with vibrant red and orange hues, focusing on the phoenix's feathers, dramatic mood"
```

---

## Example Prompt Templates

1. **Fantasy Scene**  
   ```plaintext
   /imagine "A [creature] in [magical environment], under [lighting], with [color scheme], in [art style]"
   ```  
   *Example*:  
   ```plaintext
   /imagine "A unicorn by a crystal lake at sunrise, with golden light, in a storybook style"
   ```

2. **Character Portrait**  
   ```plaintext
   /imagine "A portrait of [character], with [specific features], in [lighting], in [style]"
   ```  
   *Example*:  
   ```plaintext
   /imagine "A portrait of a wizard with a long beard, under dramatic lighting, in a dark fantasy style"
   ```

3. **Sci-Fi Scene**  
   ```plaintext
   /imagine "A [sci-fi subject] in [futuristic setting], with [specific lighting], in [style]"
   ```  
   *Example*:  
   ```plaintext
   /imagine "A robot repairing a spacecraft in a neon-lit hangar, in a cyberpunk style"
   ```

---

## Summary of Prompt Template Techniques

This chapter explored prompt templates for crafting basic, intermediate, and advanced prompts. By understanding components like subject, environment, mood, and lighting, and incorporating parameters, you can generate high-quality, visually compelling images. Mastering these techniques opens endless creative possibilities for crafting stunning visuals.

