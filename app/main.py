import re


def valid_zip_code(zip_code: str) -> bool:
    zip_code = re.sub(r"[^\d]", "", zip_code)
    valid = False
    if (
        len(zip_code) == 6
        and zip_code[0] != zip_code[2]
        and zip_code[1] != zip_code[3]
        and zip_code[2] != zip_code[4]
        and zip_code[3] != zip_code[5]
    ):
        valid = True
    return valid


def valid_zip_code_alg_2(zip_code: str) -> bool:
    zip_code = re.sub(r"[^\d]", "", zip_code)
    valid = []
    if len(zip_code) == 6:
        for i in range(0, 4):
            if zip_code[i] != zip_code[i + 2]:
                valid.append(True)
            else:
                valid.append(False)
    return all(valid or [False])
