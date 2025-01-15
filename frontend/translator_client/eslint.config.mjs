import { dirname } from 'path'
import { fileURLToPath } from 'url'
import { FlatCompat } from '@eslint/eslintrc'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const compat = new FlatCompat({
  baseDirectory: __dirname,
})

const eslintConfig = [
  ...compat.extends('next/core-web-vitals', 'next/typescript'),
  {
    rules: {
      semi: ['error', 'never'], // No semicolons
      'max-len': ['error', { code: 120, ignoreUrls: true }], // Max line length 120
      'react/prop-types': 'off', // Turn off prop-types for React
      'no-console': 'warn', // Warn on console logs
      'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }], // Warn for unused variables, ignore _ variables
      quotes: ['error', 'single'], // Enforce single quotes
      indent: ['error', 2], // Enforce 2-space indentation
    },
  },
]

export default eslintConfig
