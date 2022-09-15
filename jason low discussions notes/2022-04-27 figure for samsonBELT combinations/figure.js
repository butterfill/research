const params = {
  figures: [
    'arrow', 'avatar'
  ],
  
  positions: [
    'inside', 'outside'
  ],
  
  avatarSizeRelation: [
    'constantPixel', 'constantApparent'
  ],
  
  roomWidths: [
    'wide', 'narrow'
  ],
  
  targetObjects: [
    'glasses', 'dots'
  ],
  
  gloves: [
    'none', 'hands', 'neck', 'floor'
  ],
}

const exclusions = [
  ['figures=avatar', 'gloves']
]

const generateCombinations = (queue, res) => {
  const newRes = []
  const newQueue = [...queue]
  const paramKey = newQueue.pop()
  const alternatives = params[paramKey]
  for (let a of alternatives) {
    for (let row of res) {
      newRes.push([...row, a])
    }
  }
  if (newQueue.length) {
    return generateCombinations(newQueue, newRes)
  } else {
    return newRes
  }
}

console.log(generateCombinations(Object.keys(params), [[]]))