function replacementWarning() {
    alert("WARNING: There is a replacement for that file:\n..\\index.xml\nwhich is this HTML.\nPlease, if you want to check that XML file out again, then I'm afraid that'll be deleted and be succeeded by this HTML.\nContact:\nyoussef.land@outlook.com")
}
function namePrompt() {
    var name = prompt("What's your name?\nPlease enter it, I'm not a hacker!")
    if (name == null || name == "") {
        alert("The name was not specified.\nSorry, but without a name, you can't enter LinkedIn via this HTML.")
    } else {
        alert("Hello, " + name + "! I'm so glad you specified a name!")
    }
}