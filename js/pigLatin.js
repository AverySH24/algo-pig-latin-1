exports.translate = function(word) {
    const phrase = word.split(" ")
    let result = []
    const vowel = '^[aeiouAEIOU]'
    const consonants = '/^[^aeiou]*/g'
    const consonant_qu = '/^[^aeiou]*qu/g'
    const q = '^qu'

    for (const word of phrase) {
        let vow = word.search(vowel)
        let con = word.search(consonants) +1
        let qu = word.search(q)
        let conQu = word.search(consonant_qu)
        console.log(qu)

        if (vow !== -1){
            result.push(word+"ay")
        }
        else if (conQu !== -1){
            const slice = word.slice(conQu) + word.slice(0, conQu) + "ay";
            result.push(slice)
        }
        else if (qu !== -1){
            const slice = word.slice(qu+2) + word.slice(0, qu+2) + "ay";
            result.push(slice)
        }
        else if (con !== -1){
            const slice = word.slice(con) + word.slice(0, con) + "ay";
            result.push(slice)
        }
    }
    // console.log(result.join(" "))
    return result.join(" ")
};
