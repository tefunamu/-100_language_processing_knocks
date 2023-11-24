def cipher(messages):
    chg_msg = ""
    for i in range(len(messages)):
        if messages[i].islower():
            m_fig = 219 - ord(messages[i])
            chg_msg += chr(m_fig)
        else:
            chg_msg += messages[i]
    return chg_msg

print(cipher("I am SoftEngineer!"))
