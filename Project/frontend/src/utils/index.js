const isEmpty = function(target) {
  return target.length > 0 ? false : true;
}

const checkLogin = function() {
  return !!(sessionStorage.getItem('username') && sessionStorage.getItem('token'));
}

const checkEmail = function(email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(email).toLowerCase());
  }

const checkPassword = function(password, passwordCheck) {
      return password === passwordCheck ? true : false;
  }

export { isEmpty, checkLogin, checkEmail, checkPassword };