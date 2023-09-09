const get_year = () => {
    const today = new Date();
    return today.getFullYear();
}
document.getElementById('date').textContent = get_year();