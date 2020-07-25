var CryptoJS = require('crypto-js')
const secret = "hello my name is tulsee 12345"

export const encryptToken = token => {
  var eToken = CryptoJS.AES.encrypt(token, secret).toString()
  console.log(eToken);
}


export const decryptToken = token => {
  var byte = CryptoJS.AES.decrypt(token, secret);
  var dToken = byte.toString(CryptoJS.enc.Utf8);
  console.log(token, 'tiken')
  console.log("dtoken", byte)
  return dToken
}
