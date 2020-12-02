# How to run: awk -f myawkscript.awk myinputfile.txt

function occurencies(char, pw) {
    n = 0;
    while (p = match(pw, char)) {
        n++;
        pw = substr(pw, p + 1);
    }
    return n;
}

# --- Part 1 ---
BEGIN { FS = "[ :-]+" }

occurencies($3, $4) >= $1 && occurencies($3, $4) <= $2 {
    count1++
}

END { print "Number of correct passwords (policy with occurencies): " count1 }

# --- Part 2 ---
BEGIN { FS = "[ :-]+" }

(substr($4, $1, 1) == $3) + (substr($4, $2, 1) == $3) == 1 {
    count2++
}

END { print "Number of correct passwords (policy with indices): " count2 }
