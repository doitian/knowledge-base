# Tailwind CSS

## FAQ

┌ How to Apply Classes Via CSS

Use [@apply](https://tailwindcss.com/docs/functions-and-directives#apply=).

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  h1 {
    @apply text-2xl;
  }
  h2 {
    @apply text-xl;
  }
}

@layer components {
  .btn-blue {
    @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
  }
}

@layer utilities {
  .filter-none {
    filter: none;
  }
  .filter-grayscale {
    filter: grayscale(100%);
  }
}
```

See also other methods to [reuse styles](https://tailwindcss.com/docs/reusing-styles).
