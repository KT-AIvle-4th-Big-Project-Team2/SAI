const isKorean = (text) => {
    return text.split('').some((char) => char >= '\uAC00' && char <= '\uD7A3');
  };
  
  export default isKorean;