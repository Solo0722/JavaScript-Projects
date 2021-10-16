function generate(){
    let quotes = {
        "- Richard Bach":'"If you love someone, set them free. If they come back they\'re yours; if they don\'t they never were."',
        "- Warren E. Burger": '"Free speech carries with it some freedom to listen."',
        "- Albert Camus": '"The only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion."',
        "- James A. Garfield": "The truth will set you free, but first it will make you miserable.",
        "- John Stuart Mill": '"A man who has nothing for which he is willing to fight, nothing which is more important than his own personal safety, is a miserable creature and has no chance of being free unless made and kept so by the exertions of better men than himself."',
        "- Ezra Pound": '"A slave is one who waits for someone to come and free him."'
    }

    let authors = Object.keys(quotes);
    let author = authors[Math.floor(Math.random()*authors.length)];

    let quote = quotes[author];

    document.getElementById("quote").innerHTML = quote;
    document.getElementById("author").innerHTML = author;
}