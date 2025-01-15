'use client'

import React, { useState } from 'react'
import { useForm, SubmitHandler } from 'react-hook-form'
import styles from './translator.module.scss'

interface IFormInputs {
  text: string
  lang_pair: string
  model: string
}

export default function Translator() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IFormInputs>()
  const [translation, setTranslation] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const onSubmit: SubmitHandler<IFormInputs> = async (data) => {
    setIsLoading(true)
    setError('')

    try {
      const response = await fetch('/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`)
      }

      const responseData = await response.json()
      setTranslation(responseData.translation[0])
    } catch {
      setError('Something went wrong. Please try again.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className={styles.translator}>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className={styles.form_group}>
          <label htmlFor="langPair">Language Pair</label>
          <select id="langPair" {...register('lang_pair')}>
            <option value="en-de">en-de</option>
            <option value="en-ru">en-ru</option>
            <option value="de-ru">de-ru</option>
          </select>
        </div>

        <div className={styles.form_group}>
          <label htmlFor="model">Model</label>
          <select id="model" {...register('model')}>
            <option value="Helsinki-NLP">Helsinki-NLP</option>
            <option value="facebook-nllb">facebook-nllb</option>
          </select>
        </div>

        <div className={styles.form_group}>
          <label htmlFor="text">Text to Translate</label>
          <textarea id="text" rows={4} {...register('text', { required: 'Fill this field' })} />
          {errors.text && <p className={styles.error_message}>{errors.text.message}</p>}
        </div>

        <button type="submit" className={styles.submit_btn} disabled={isLoading}>
          {isLoading ? 'Translating...' : 'Translate'}
        </button>
      </form>

      <div>
        {error && <p className={styles.error_message}>{error}</p>}
        {translation && (
          <div className={styles.translation_result}>
            <label>Translation</label>
            <textarea disabled value={translation} rows={4} />
          </div>
        )}
      </div>
    </div>
  )
}
