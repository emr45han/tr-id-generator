def verifySequence(idNumber: str):
    # Stage 1
    if len(idNumber) == 11:
        # Stage 2
        if type(idNumber) == str:
            try:
                int(idNumber)

            except:
                return False

            # Stage 3
            if idNumber.find("0") != 0:
                # Stage 4
                first = int(idNumber[0:1])
                second = int(idNumber[1:2])
                third = int(idNumber[2:3])
                fourth = int(idNumber[3:4])
                fifth = int(idNumber[4:5])
                sixth = int(idNumber[5:6])
                seventh = int(idNumber[6:7])
                eighth = int(idNumber[7:8])
                ninth = int(idNumber[8:9])
                tenth = int(idNumber[9:10])
                eleventh = int(idNumber[10:11])

                stage_4 = ((first + third + fifth + seventh + ninth) * 7 - (second + fourth + sixth + eighth)) % 10
                if tenth == stage_4:
                    # Stage 5
                    stage_5 = (first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth) % 10
                    if eleventh == stage_5:
                        return True

                    else:
                        return False
                else:
                    return False
            else:
                return False

    else:
        return False


def idGenerator(value):
    if type(value) == str:
        try:
            int(value)

        except:
            return False

    if value.find("0") == 0:
        return False

    first = int(value[0:1])
    second = int(value[1:2])
    third = int(value[2:3])
    fourth = int(value[3:4])
    fifth = int(value[4:5])
    sixth = int(value[5:6])
    seventh = int(value[6:7])
    eighth = int(value[7:8])
    ninth = int(value[8:9])

    tenth = ((first + third + fifth + seventh + ninth) * 7 - (second + fourth + sixth + eighth)) % 10
    eleventh = (first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth) % 10

    return f"{first}{second}{third}{fourth}{fifth}{sixth}{seventh}{eighth}{ninth}{tenth}{eleventh}"

i = 100000000
file = open("working_identities.txt", "w")
while i < 1000000000:
    string_i = str(i)
    id = idGenerator(string_i)
    if verifySequence(id):
        file.write(f"{id}\n")
        i += 1
file.close()

