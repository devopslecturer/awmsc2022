/* Sliding Animation */

const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

const signUpSlide = document.getElementById("mobile-up");
const signInSlide = document.getElementById("mobile-in");
const signUpContainer = document.getElementById("sign-up-container");
const signInContainer = document.getElementById("sign-in-container");

signUpSlide.addEventListener("click", () => {
  signUpContainer.style.opacity = 1;
  signUpContainer.style.zIndex = 5;
  signInContainer.style.opacity = 0;
  signInContainer.style.zIndex = 2;
});

signInSlide.addEventListener("click", () => {
  signInContainer.style.opacity = 1;
  signInContainer.style.zIndex = 5;
  signUpContainer.style.opacity = 0;
  signUpContainer.style.zIndex = 2;
});

/*Sign Up Validation*/

const su_name = document.getElementById("su-name");
const su_mail = document.getElementById("su-mail");
const su_pass = document.getElementById("su-pass");
const su_pass_re = document.getElementById("su-pass-re");

var regName = /^[a-zA-Z]+ [a-zA-Z]+$/;
var regMail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

su_name.addEventListener("input", () => {
  if (regName.test(su_name.value)) {
    document.getElementById("su-name-check").style.display = "inline";
  } else {
    document.getElementById("su-name-check").style.display = "none";
  }
});

su_mail.addEventListener("input", () => {
  if (regMail.test((m = su_mail.value))) {
    document.getElementById("su-mail-check").style.display = "inline";
  } else {
    document.getElementById("su-mail-check").style.display = "none";
  }
});

const togglePassword = document.getElementById("su-pass-show");
const itag = document.querySelector(".input-field i#togglePassword");
const su_pass_inp = document.getElementById("su-pass");
togglePassword.addEventListener("click", () => {
  if (itag.classList.contains("fa-eye")) {
    itag.classList.remove("fa-eye");
    itag.classList.add("fa-eye-slash");
  } else {
    itag.classList.remove("fa-eye-slash");
    itag.classList.add("fa-eye");
  }
  const type =
    su_pass_inp.getAttribute("type") === "password" ? "text" : "password";
  su_pass_inp.setAttribute("type", type);
  togglePassword.innerHTML = "";
  togglePassword.appendChild(itag);
});

const togglePasswordRe = document.getElementById("su-pass-re-show");
const itagre = document.querySelector(".input-field i#togglePasswordRe");
const su_pass_re_inp = document.getElementById("su-pass-re");
togglePasswordRe.addEventListener("click", () => {
  if (itagre.classList.contains("fa-eye")) {
    itagre.classList.remove("fa-eye");
    itagre.classList.add("fa-eye-slash");
  } else {
    itagre.classList.remove("fa-eye-slash");
    itagre.classList.add("fa-eye");
  }
  const typere =
    su_pass_re_inp.getAttribute("type") === "password" ? "text" : "password";
  su_pass_re_inp.setAttribute("type", typere);
  togglePasswordRe.innerHTML = "";
  togglePasswordRe.appendChild(itagre);
});

function scorePassword(pass) {
  var score = 0;
  if (!pass) return score;

  // award every unique letter until 5 repetitions
  var letters = new Object();
  for (var i = 0; i < pass.length; i++) {
    letters[pass[i]] = (letters[pass[i]] || 0) + 1;
    score += 5.0 / letters[pass[i]];
  }

  // bonus points for mixing it up
  var variations = {
    digits: /\d/.test(pass),
    lower: /[a-z]/.test(pass),
    upper: /[A-Z]/.test(pass),
    nonWords: /\W/.test(pass)
  };

  var variationCount = 0;
  for (var check in variations) {
    variationCount += variations[check] == true ? 1 : 0;
  }
  score += (variationCount - 1) * 10;

  return parseInt(score);
}

su_pass.addEventListener("input", () => {
  var score = scorePassword(su_pass.value);
  var parent = document.getElementById("su-pass-parent");
  parent.removeAttribute("class");
  parent.classList.add("input-field");
  if (score > 80) {
    parent.classList.add("strong");
    parent.classList.remove("medium");
  } else if (score > 60) {
    parent.classList.add("medium");
    parent.classList.remove("weak");
  } else if (score >= 30) {
    parent.classList.add("weak");
  }
});

su_pass_re.addEventListener("input", () => {
  if (su_pass.value == su_pass_re.value) {
    document.getElementById("su-pass-re-show").style.display = "inline";
  } else {
    document.getElementById("su-pass-re-show").style.display = "";
  }
});

document.getElementById("sign-up-btn").addEventListener("click", () => 
{
 /* if (
    document.getElementById("su-name-check").style.display == "" ||
    document.getElementById("su-name-check").style.display == "none"
  ) {
    document.getElementById("error-msg-signup").innerHTML =
      "<i class='fa fa-times-circle'></i> Please enter a valid username.";
    document.getElementById("error-msg-signup").style.display = "block";
  } else if (
    document.getElementById("su-mail-check").style.display == "" ||
    document.getElementById("su-mail-check").style.display == "none"
  ) {
    document.getElementById("error-msg-signup").innerHTML =
      "<i class='fa fa-times-circle'></i> Please enter a valid Email Address.";
    document.getElementById("error-msg-signup").style.display = "block";
  } else if (
    document.getElementById("su-pass-parent").classList.contains("weak") |
    (su_pass.value == "")
  ) {
    document.getElementById("error-msg-signup").innerHTML =
      "<i class='fa fa-times-circle'></i> Your password is too weak.";
    document.getElementById("error-msg-signup").style.display = "block";
  } else*/
    if (su_pass.value != su_pass_re.value) {
    document.getElementById("error-msg-signup").innerHTML =
      "<i class='fa fa-times-circle'></i> Passwords don't match.";
    document.getElementById("error-msg-signup").style.display = "block";
  } else {
    document.getElementById("error-msg-signup").style.display = "";
  }
});