'use client';

import { useState } from 'react';
import styles from './page.module.css';

const EDITING_MODES = [
  {
    id: 'critique',
    name: 'Manuscript Critique',
    description: 'High-level feedback on story, characters, plot, and pacing',
    icon: '📖'
  },
  {
    id: 'line_edit',
    name: 'Line Edit',
    description: 'Sentence-level improvements for flow, clarity, and voice',
    icon: '✍️'
  },
  {
    id: 'copyedit',
    name: 'Copyedit',
    description: 'Grammar, style, consistency, and accuracy checks',
    icon: '📝'
  },
  {
    id: 'proofread',
    name: 'Proofread',
    description: 'Final error detection including spelling, typos, and punctuation',
    icon: '🔍'
  }
];

export default function Home() {
  const [selectedMode, setSelectedMode] = useState('critique');
  const [manuscriptText, setManuscriptText] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!manuscriptText.trim()) {
      setError('Please enter some text to edit');
      return;
    }

    setLoading(true);
    setError(null);
    setFeedback(null);

    try {
      const response = await fetch('http://localhost:8000/api/edit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: manuscriptText,
          mode: selectedMode
        })
      });

      if (!response.ok) {
        throw new Error('Failed to process manuscript');
      }

      const data = await response.json();
      setFeedback(data);
    } catch (err) {
      setError(err.message || 'An error occurred while processing your manuscript');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <h1 className={styles.title}>📚 Seventeen Pages</h1>
        <p className={styles.subtitle}>AI-Powered Manuscript Editing</p>
      </header>

      <div className={styles.container}>
        {/* Mode Selection */}
        <section className={styles.modeSection}>
          <h2 className={styles.sectionTitle}>Choose Your Editing Mode</h2>
          <div className={styles.modeGrid}>
            {EDITING_MODES.map((mode) => (
              <button
                key={mode.id}
                className={`${styles.modeCard} ${selectedMode === mode.id ? styles.modeCardActive : ''}`}
                onClick={() => setSelectedMode(mode.id)}
              >
                <div className={styles.modeIcon}>{mode.icon}</div>
                <h3 className={styles.modeName}>{mode.name}</h3>
                <p className={styles.modeDescription}>{mode.description}</p>
              </button>
            ))}
          </div>
        </section>

        {/* Text Input */}
        <section className={styles.inputSection}>
          <h2 className={styles.sectionTitle}>Your Manuscript</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              className={styles.textarea}
              value={manuscriptText}
              onChange={(e) => setManuscriptText(e.target.value)}
              placeholder="Paste your manuscript text here..."
              rows={12}
            />
            <button 
              type="submit" 
              className={styles.submitButton}
              disabled={loading}
            >
              {loading ? 'Processing...' : `Get ${EDITING_MODES.find(m => m.id === selectedMode)?.name}`}
            </button>
          </form>
        </section>

        {/* Error Message */}
        {error && (
          <div className={styles.error}>
            <p>⚠️ {error}</p>
          </div>
        )}

        {/* Feedback Display */}
        {feedback && (
          <section className={styles.feedbackSection}>
            <h2 className={styles.sectionTitle}>
              {EDITING_MODES.find(m => m.id === feedback.mode)?.icon} Feedback
            </h2>
            <div className={styles.feedbackContent}>
              <div className={styles.feedbackText}>
                {feedback.feedback.split('\n').map((line, index) => (
                  <p key={index}>{line}</p>
                ))}
              </div>
              
              {feedback.suggestions && feedback.suggestions.length > 0 && (
                <div className={styles.suggestions}>
                  <h3>Key Suggestions:</h3>
                  <ul>
                    {feedback.suggestions.map((suggestion, index) => (
                      <li key={index}>{suggestion}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </section>
        )}
      </div>

      <footer className={styles.footer}>
        <p>© 2024 Seventeen & Willow Press. Refining every page with heart and precision.</p>
      </footer>
    </main>
  );
}
