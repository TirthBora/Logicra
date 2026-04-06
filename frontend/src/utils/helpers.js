export const formatSimilarity = (score) => `${(score * 100).toFixed(1)}%`

export const truncate = (str, length = 50) => 
  str.length > length ? str.slice(0, length) + '...' : str

export const fileTypeIcon = (fileName) => {
  if (fileName.endsWith('.py')) return '🐍'
  if (fileName.endsWith('.js')) return '📜'
  return '📄'
}

