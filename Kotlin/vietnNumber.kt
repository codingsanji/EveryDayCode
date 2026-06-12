fun translate(num: Int): String {
    if ((num >= 0) and (num <= 9)) {
        return when (num) {
            0 -> "Không"
            1 -> "Một"
            2 -> "Hai"
            3 -> "Ba"
            4 -> "Bốn"
            5 -> "Năm"
            6 -> "Sáu"
            7 -> "Bảy"
            8 -> "Tám"
            9 -> "Chín"
            else -> error("Invalid digit")
        }
    }
    
    if (num == 10) return "Mười"
    
    val tenth = num / 10
    val digit = num % 10
   
    if ((num > 10) and (num <= 19)) {
        return "Mười ${translate(digit)}"
    }
    
    val translatedDigit = when (digit) {
        0 -> ""
        1 -> "Mốt"
        else -> translate(digit)
    }
    
    return "${translate(tenth)} Mươi $translatedDigit"
}
fun main() {
    for (num in 0..99) {
        println(translate(num))
    }
}