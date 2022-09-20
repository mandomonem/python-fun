function replacementWarning() {
    console.warn("WARNING: There is a replacement for that file:\n..\\index.xml\nwhich is this HTML.\nPlease, if you want to check that XML file out again, then I'm afraid that's been deleted and has been succeeded by this HTML.\nE-mail address:\nyoussef.land@outlook.com")
}
function linkedinNamePrompt() {
    var name = prompt("What's your name?\nPlease enter it, I'm not a hacker!")
    if (name == null || name == "") {
        alert("The name was not specified.\nSorry, but without a name, you can't enter LinkedIn via this HTML.")
    } else {
        alert("Hello, " + name + "! I'm so glad you specified a name! Click OK to go to LinkedIn!")
        linkedinRedirect();
    }
}
function linkedinRedirect() {
    location.href = "https://linkedin.com/feed";
}