# GenAI for Beginners – Documentation Site

## 📘 Project Overview

This is a **Next.js-based documentation website** created using the **Fumadocs framework**. It serves as an educational resource for learning about **Generative AI (GenAI)** from scratch. The project is optimized for clear, interactive, and modern documentation delivery.

## 🔧 Key Features

- **Built with Next.js**: Uses the React-based framework for server-side rendering and fast static builds.
- **Powered by Fumadocs**:
  - `fumadocs-core`, `fumadocs-mdx`, and `fumadocs-ui` manage content, markdown rendering, and UI components.
  - Full support for MDX to combine markdown and JSX.
- **Interactive Content**:
  - Supports diagrams via Mermaid (`@theguild/remark-mermaid`).
  - Math rendering using `remark-math` and `rehype-katex`.
- **Styling**: Tailwind CSS configured with Fumadocs presets and PostCSS.
- **TypeScript & ESLint**: Strict typing and code linting enabled.

## 🧩 Technical Stack

- **Framework**: Next.js 15.x
- **Language**: TypeScript
- **Styling**: Tailwind CSS with custom presets from `fumadocs-ui`
- **Content Format**: `.mdx` with plugin support
- **Linting**: ESLint using Next.js presets

## 📁 Configuration Highlights

- `next.config.mjs`: Integrates MDX and enables React strict mode.
- `tailwind.config.js`: Sets up dark mode and Fumadocs UI presets.
- `postcss.config.mjs`: Loads Tailwind via PostCSS.
- `tsconfig.json`: TypeScript paths, JSX settings, and strict compiler options.
- `.eslintrc.json`: Next.js ESLint rules for consistent development.

## 🚀 Getting Started (Development Only)

> ⚠️ **Do not push any code to this repository.** This is a configuration and setup base only.

To preview the site locally:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Visit `http://localhost:3000` in your browser.

## 🧠 Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Fumadocs Documentation](https://fumadocs.vercel.app)
- [Tailwind CSS Docs](https://tailwindcss.com)