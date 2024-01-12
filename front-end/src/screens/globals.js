// globals.js
// globals.js
const globalData = {};

export function setGlobalData(key, value) {
  globalData[key] = value;
}

export function getGlobalData(key) {
  return globalData[key];
}

// globals.js
export function getAllGlobalData() {
    return globalData;
  }
  