const body = document.body;
const checkbox = document.getElementById('toggler')
const darksheet = document.getElementById('darksheet')
const mql = window.matchMedia("(prefers-color-scheme: dark)");
const userPrefersDark = window.matchMedia && mql.matches;

function setCookieDark(value) {
    document.cookie = "dark=" + value + "; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/; Secure; SameSite=None";
}

function disableDark() {
    setCookieDark("false")
    checkbox.checked = false;
    darksheet.disabled = true;
}

function enableDark() {
    setCookieDark("true")
    checkbox.checked = true;
    darksheet.disabled = false;
}

mql.addEventListener("change", (event) => {
    if (event.matches) {
        enableDark();
    } else {
        disableDark();
    }
})

checkbox.addEventListener('change', (event) => {
    if (event.target.checked) {
        enableDark();
    } else {
        disableDark();
    }
})

if (document.cookie) {
    const darkRemember = document.cookie
        .split('; ')
        .find(row => row.startsWith('dark'))
        .split('=')[1];
    if (darkRemember === "true") {
        enableDark();
    }
} else {
    if (userPrefersDark) {
        enableDark();
    } else {
        disableDark();
    }
}
