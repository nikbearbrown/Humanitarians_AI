# Humanitarians.ai Website Revamp

Build with V0 by Vercel using TypeScript and React (TSX)

## 🧩 Overview
This document outlines the project structure, contribution guidelines, and component responsibilities for the revamp of https://www.humanitarians.ai using the Bento template and inspiration from Fylla.

## 🧑‍💻 Contribution Guidelines

### ✅ Component Ownership
* Each contributor should **claim a component** by putting their name next to it in this document or the project tracker.
* **Work only within your component folder** and do not modify others' code without collaboration.

### 💻 Coding Standards
* **Framework**: React + TypeScript (.tsx)
* **Styling**: TailwindCSS (preferred), or modular SCSS if needed.
* **Naming**:
   * Use **PascalCase** for components (e.g., BlogCard.tsx).
   * Use **camelCase** for variables and function names.
* **Folder Structure**: One folder per component, including its .tsx, .module.css/.ts, test files, and assets if needed.
* **Commit Messages**: Use meaningful commits. Example: feat: add HeroSection component

### 📐 Project Rules
* All pages are **static**.
* Follow **modular development** – build components as reusable blocks.
* Respect the file structure.
* Add your name to your component in this README.

## 📁 Project Structure
```
/project-root
│
├── components/
│   ├── Header/
│   │   └── Header.tsx
│   ├── Footer/
│   ├── HeroSection/
│   ├── BlogCard/
│   ├── ProjectCard/
│   └── ...
│
├── pages/
│   ├── index.tsx
│   ├── about.tsx
│   ├── services.tsx
│   ├── projects.tsx
│   ├── blog.tsx
│   ├── donate.tsx
│   └── contact.tsx
│
├── public/
│   └── assets/
│       ├── images/
│       └── logos/
│
├── styles/
│   └── globals.css
│
├── utils/
│   └── api.ts
│
├── data/
│   ├── blogPosts.json
│   └── projects.json
│
├── types/
│   └── index.ts
│
├── README.md
└── tsconfig.json
```

## 🔧 Components to Build

| **Component** | **Description** | **Assigned To** |
|---------------|-----------------|-----------------|
| Header | Top navigation bar | |
| Footer | Global footer | |
| HeroSection | Intro section on main page | |
| FeaturedWork | Carousel or grid for featured projects | |
| WhatWeDo | Mission summary and core activities | |
| LatestNews | Recent blogs or news cards | |
| BlogCard | Individual blog preview | |
| ProjectCard | Summary of a project | |
| DonationSection | Content + payment gateway options | |
| ContactForm | Form + contact details | |
| AboutTeam | Team member profiles | |
| ValuesSection | Organizational values | |
| JourneyTimeline | Visual timeline of org history | |
| ServicesOverview | Mentorship/fellowship program summary + CTAs | |
| Testimonials | Donor/mentee quotes and experiences | |
| CTASection | Reusable call-to-action block | |

## ✨ Tips for Success
* Keep components **atomic** – small, focused, and composable.
* Maintain **accessibility** (ARIA labels, keyboard support).
* Use **TypeScript interfaces** for all props.
* Leverage **V0-generated code** but refactor for reusability and DRYness.
* Test your component in isolation before integration.

Let's build something meaningful together! 🚀

## Appendix: TSX and Tailwind CSS Guide for Humanitarians.ai

### Understanding TSX

TSX (TypeScript JSX) is a syntax extension for TypeScript that allows you to write React components with type safety. It combines the power of TypeScript for static type checking with JSX for writing HTML-like syntax in JavaScript.

#### Key TSX Concepts

##### 1. Component Structure

A basic TSX component looks like this:

```tsx
import React from 'react';

interface HeroProps {
  title: string;
  subtitle?: string; // Optional prop
  onCtaClick: () => void;
}

const HeroSection: React.FC<HeroProps> = ({ title, subtitle, onCtaClick }) => {
  return (
    <div className="hero">
      <h1>{title}</h1>
      {subtitle && <p>{subtitle}</p>}
      <button onClick={onCtaClick}>Learn More</button>
    </div>
  );
};

export default HeroSection;
```

##### 2. Type Definitions

Define interfaces for your data structures:

```tsx
// types/index.ts
export interface BlogPost {
  id: string;
  title: string;
  excerpt: string;
  content: string;
  author: TeamMember;
  publishDate: string;
  tags: string[];
}

export interface TeamMember {
  id: string;
  name: string;
  role: string;
  bio: string;
  imageUrl: string;
  socialLinks?: {
    twitter?: string;
    linkedin?: string;
    github?: string;
  };
}
```

##### 3. Using TypeScript with Props

```tsx
// Consuming typed props
import { BlogPost } from '../types';

interface BlogCardProps {
  post: BlogPost;
  isHighlighted?: boolean;
}

const BlogCard: React.FC<BlogCardProps> = ({ post, isHighlighted = false }) => {
  // Component implementation
};
```

### Tailwind CSS Essentials

Tailwind CSS is a utility-first CSS framework that allows you to build designs directly in your markup by composing utility classes.

#### Key Tailwind Concepts

##### 1. Basic Utility Classes

```tsx
// Example component with Tailwind classes
const Button: React.FC<ButtonProps> = ({ label, variant = 'primary', onClick }) => {
  return (
    <button 
      className={`
        px-4 py-2 rounded-md font-medium transition-colors
        ${variant === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-700' : ''}
        ${variant === 'secondary' ? 'bg-gray-200 text-gray-800 hover:bg-gray-300' : ''}
        ${variant === 'ghost' ? 'bg-transparent text-blue-600 hover:bg-blue-50' : ''}
      `}
      onClick={onClick}
    >
      {label}
    </button>
  );
};
```

##### 2. Responsive Design

Tailwind makes responsive design simple with breakpoint prefixes:

```tsx
<div className="
  w-full         // Mobile (default)
  md:w-1/2       // Medium screens (768px+)
  lg:w-1/3       // Large screens (1024px+)
  p-4            // Padding on all screens
  md:p-6         // More padding on medium screens
">
  Content here
</div>
```

#### 3. Common Patterns for Humanitarians.ai

##### Card Component

```tsx
<div className="bg-white rounded-lg shadow-md overflow-hidden">
  <img src={imageUrl} alt={title} className="w-full h-48 object-cover" />
  <div className="p-4">
    <h3 className="text-xl font-semibold text-gray-800">{title}</h3>
    <p className="mt-2 text-gray-600">{excerpt}</p>
    <div className="mt-4 flex justify-between items-center">
      <span className="text-sm text-gray-500">{formatDate(date)}</span>
      <button className="text-blue-600 hover:text-blue-800">Read More →</button>
    </div>
  </div>
</div>
```

##### Hero Section

```tsx
<section className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white">
  <div className="container mx-auto px-4 py-16 md:py-24">
    <div className="max-w-2xl">
      <h1 className="text-4xl md:text-5xl font-bold leading-tight">
        Empowering Humanitarian Efforts with AI
      </h1>
      <p className="mt-4 text-xl text-blue-100">
        Connecting technology experts with humanitarian organizations to solve global challenges.
      </p>
      <div className="mt-8 flex flex-wrap gap-4">
        <button className="bg-white text-blue-700 px-6 py-3 rounded-md font-medium hover:bg-blue-50">
          Get Involved
        </button>
        <button className="bg-transparent border border-white text-white px-6 py-3 rounded-md font-medium hover:bg-white/10">
          Learn More
        </button>
      </div>
    </div>
  </div>
</section>
```

### Best Practices for the Humanitarians.ai Project

#### 1. Component Organization

```
/components
  /common
    /Button
      Button.tsx
      Button.test.tsx
    /Card
      Card.tsx
      Card.test.tsx
  /layout
    /Header
      Header.tsx
    /Footer
      Footer.tsx
  /sections
    /HeroSection
      HeroSection.tsx
    /FeaturedWork
      FeaturedWork.tsx
```

#### 2. Tailwind Configuration

Create a `tailwind.config.js` file to customize your theme:

```js
// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'hai-blue': {
          50: '#f0f7ff',
          100: '#e0efff',
          500: '#3b82f6',
          700: '#1d4ed8',
          900: '#1e3a8a',
        },
        'hai-neutral': {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          700: '#374151',
          900: '#111827',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

#### 3. Styling Strategies

##### Consistent Component Styling

```tsx
// Consistent button styling approach
const Button: React.FC<ButtonProps> = ({ 
  label, 
  variant = 'primary',
  size = 'medium',
  fullWidth = false,
  onClick 
}) => {
  const baseClasses = "font-medium rounded transition-colors focus:outline-none focus:ring-2";
  
  const variantClasses = {
    primary: "bg-hai-blue-700 text-white hover:bg-hai-blue-800 focus:ring-hai-blue-500",
    secondary: "bg-hai-neutral-200 text-hai-neutral-700 hover:bg-hai-neutral-300 focus:ring-hai-neutral-400",
    ghost: "bg-transparent text-hai-blue-700 hover:bg-hai-blue-50 focus:ring-hai-blue-500"
  };
  
  const sizeClasses = {
    small: "px-3 py-1.5 text-sm",
    medium: "px-4 py-2",
    large: "px-6 py-3 text-lg"
  };
  
  return (
    <button 
      className={`
        ${baseClasses}
        ${variantClasses[variant]}
        ${sizeClasses[size]}
        ${fullWidth ? 'w-full' : ''}
      `}
      onClick={onClick}
    >
      {label}
    </button>
  );
};
```

#### 4. Working with Data

```tsx
// pages/blog.tsx
import { useState, useEffect } from 'react';
import { BlogPost } from '../types';
import BlogCard from '../components/BlogCard/BlogCard';

const BlogPage: React.FC = () => {
  const [posts, setPosts] = useState<BlogPost[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        // In a real application, this would be an API call
        const response = await fetch('/api/blog-posts');
        const data = await response.json();
        setPosts(data);
      } catch (error) {
        console.error('Error fetching blog posts:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchPosts();
  }, []);
  
  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }
  
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold mb-8">Latest Blog Posts</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map(post => (
          <BlogCard key={post.id} post={post} />
        ))}
      </div>
    </div>
  );
};

export default BlogPage;
```

### Useful TSX & Tailwind Resources

1. **TypeScript React Cheat Sheet**: [TypeScript React Cheat Sheet](https://github.com/typescript-cheatsheets/react)
2. **Tailwind CSS Documentation**: [Tailwind CSS Docs](https://tailwindcss.com/docs)
3. **React TypeScript Starter**: [Create React App TypeScript](https://create-react-app.dev/docs/adding-typescript/)
4. **Tailwind UI Components**: [Tailwind UI](https://tailwindui.com/) (paid resource)
5. **Free Tailwind Components**: [Tailwind Components](https://tailwindcomponents.com/)

### Common Gotchas and Solutions

#### 1. TypeScript Props Validation

**Problem**: Forgetting to validate optional props or using incorrect types.

**Solution**:
```tsx
// Bad
interface CardProps {
  title: string;
  description: string; // Could be null or undefined in real data
}

// Good
interface CardProps {
  title: string;
  description?: string; // Mark as optional
  imageUrl: string | null; // Allow null values
  onClick?: () => void; // Optional event handler
}
```

#### 2. Tailwind Class Organization

**Problem**: Long strings of Tailwind classes become unmanageable.

**Solution**: Group related classes with template literals:
```tsx
<div className={`
  // Layout
  flex flex-col items-center
  // Spacing
  p-4 my-8
  // Colors
  bg-white text-gray-800
  // Effects
  shadow-md rounded-lg hover:shadow-lg
  // Responsive
  md:flex-row md:p-6
`}>
  {/* Content here */}
</div>
```

#### 3. Component Reusability

**Problem**: Creating overly specific components that are hard to reuse.

**Solution**: Use composition and props for flexibility:
```tsx
// Card.tsx - Base reusable card component
const Card: React.FC<CardProps> = ({ 
  children, 
  padding = 'normal',
  withShadow = true,
  className = '' 
}) => {
  const paddingClasses = {
    'none': '',
    'small': 'p-2',
    'normal': 'p-4',
    'large': 'p-6'
  };
  
  return (
    <div className={`
      bg-white rounded-lg
      ${paddingClasses[padding]}
      ${withShadow ? 'shadow-md' : ''}
      ${className}
    `}>
      {children}
    </div>
  );
};

// Usage
<Card padding="large" className="border border-gray-200">
  <h3>Card Title</h3>
  <p>Card content goes here...</p>
</Card>
```
