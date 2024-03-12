
def add_space(text: str):
    count = 0
    indices = list()
    for i, c in enumerate(text):
        if c == ' ':
            indices.append(i)
    mul = 77
    out = list()
    current = 0
    for i in range(len(indices)-1):
        k = current + mul
        if (k <= indices[i] and k < indices[i + 1]):
            out.append(indices[i])
            current = indices[i]
        count+=1
    final_out = ""
    l = len(text)
    out.append(l)
    final_out += (text[:out[0]] + '\n')
    for i in range(len(out) - 1):
        final_out += (text[out[i] + 1:out[i + 1]] + '\n')
    return final_out