import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    way = list(map(str,input().split()))
    cubeU = [['w','w','w'],['w','w','w'],['w','w','w']]
    cubeD = [['y','y','y'],['y','y','y'],['y','y','y']]
    cubeF = [['r','r','r'],['r','r','r'],['r','r','r']]
    cubeB = [['o','o','o'],['o','o','o'],['o','o','o']]
    cubeL = [['g','g','g'],['g','g','g'],['g','g','g']]
    cubeR = [['b','b','b'],['b','b','b'],['b','b','b']]

    while way:
        if way[0][0] == 'U':
            tempF = cubeF[0]
            tempL = cubeL[0]
            tempB = cubeB[0]
            tempR = cubeR[0]
            tempU_column1 = [cubeU[0][0], cubeU[1][0], cubeU[2][0]]
            tempU_column2 = [cubeU[0][1], cubeU[1][1], cubeU[2][1]]
            tempU_column3 = [cubeU[0][2], cubeU[1][2], cubeU[2][2]]

            if way[0][1] == '+':
                cubeF[0] = tempR
                cubeL[0] = tempF
                cubeB[0] = tempL
                cubeR[0] = tempB
                cubeU[0] = [tempU_column1[2], tempU_column1[1], tempU_column1[0]]
                cubeU[1] = [tempU_column2[2], tempU_column2[1], tempU_column2[0]]
                cubeU[2] = [tempU_column3[2], tempU_column3[1], tempU_column3[0]]
            elif way[0][1] == '-':
                cubeF[0] = tempL
                cubeL[0] = tempB
                cubeB[0] = tempR
                cubeR[0] = tempF
                cubeU[0] = tempU_column3
                cubeU[1] = tempU_column2
                cubeU[2] = tempU_column1

        elif way[0][0] == 'D':
            tempF = cubeF[2]
            tempL = cubeL[2]
            tempB = cubeB[2]
            tempR = cubeR[2]
            tempD_column1 = [cubeD[0][0], cubeD[1][0], cubeD[2][0]]
            tempD_column2 = [cubeD[0][1], cubeD[1][1], cubeD[2][1]]
            tempD_column3 = [cubeD[0][2], cubeD[1][2], cubeD[2][2]]

            if way[0][1] == '+':
                cubeF[2] = tempL
                cubeL[2] = tempB
                cubeB[2] = tempR
                cubeR[2] = tempF
                cubeD[0] = [tempD_column1[2], tempD_column1[1], tempD_column1[0]]
                cubeD[1] = [tempD_column2[2], tempD_column2[1], tempD_column2[0]]
                cubeD[2] = [tempD_column3[2], tempD_column3[1], tempD_column3[0]]
            elif way[0][1] == '-':
                cubeF[2] = tempR
                cubeL[2] = tempF
                cubeB[2] = tempL
                cubeR[2] = tempB
                cubeD[0] = tempD_column3
                cubeD[1] = tempD_column2
                cubeD[2] = tempD_column1

        elif way[0][0] == 'F':
            tempU = cubeU[2]
            tempL = [cubeL[0][2], cubeL[1][2], cubeL[2][2]]
            tempD = cubeD[0]
            tempR = [cubeR[0][0], cubeR[1][0], cubeR[2][0]]
            tempF_column1 = [cubeF[0][0], cubeF[1][0], cubeF[2][0]]
            tempF_column2 = [cubeF[0][1], cubeF[1][1], cubeF[2][1]]
            tempF_column3 = [cubeF[0][2], cubeF[1][2], cubeF[2][2]]

            if way[0][1] == '+':
                cubeU[2] = [tempL[2], tempL[1], tempL[0]]
                cubeL[0][2], cubeL[1][2], cubeL[2][2] = tempD[0], tempD[1], tempD[2]
                cubeD[0] = [tempR[2], tempR[1], tempR[0]]
                cubeR[0][0], cubeR[1][0], cubeR[2][0] = tempU[0], tempU[1], tempU[2]
                cubeF[0] = [tempF_column1[2], tempF_column1[1], tempF_column1[0]]
                cubeF[1] = [tempF_column2[2], tempF_column2[1], tempF_column2[0]]
                cubeF[2] = [tempF_column3[2], tempF_column3[1], tempF_column3[0]]
            elif way[0][1] == '-':
                cubeU[2] = tempR
                cubeL[0][2], cubeL[1][2], cubeL[2][2] = tempU[2], tempU[1], tempU[0]
                cubeD[0] = tempL
                cubeR[0][0], cubeR[1][0], cubeR[2][0] = tempD[2], tempD[1], tempD[0]
                cubeF[0] = tempF_column3
                cubeF[1] = tempF_column2
                cubeF[2] = tempF_column1

        elif way[0][0] == 'B':
            tempU = cubeU[0]
            tempL = [cubeL[0][0], cubeL[1][0], cubeL[2][0]]
            tempD = cubeD[2]
            tempR = [cubeR[0][2], cubeR[1][2], cubeR[2][2]]
            tempB_column1 = [cubeB[0][0], cubeB[1][0], cubeB[2][0]]
            tempB_column2 = [cubeB[0][1], cubeB[1][1], cubeB[2][1]]
            tempB_column3 = [cubeB[0][2], cubeB[1][2], cubeB[2][2]]

            if way[0][1] == '+':
                cubeU[0] = tempR
                cubeL[0][0], cubeL[1][0], cubeL[2][0] = tempU[2], tempU[1], tempU[0]
                cubeD[2] = tempL
                cubeR[0][2], cubeR[1][2], cubeR[2][2] = tempD[2], tempD[1], tempD[0]
                cubeB[0] = [tempB_column1[2], tempB_column1[1], tempB_column1[0]]
                cubeB[1] = [tempB_column2[2], tempB_column2[1], tempB_column2[0]]
                cubeB[2] = [tempB_column3[2], tempB_column3[1], tempB_column3[0]]

            elif way[0][1] == '-':
                cubeU[0] = [tempL[2], tempL[1], tempL[0]]
                cubeL[0][0], cubeL[1][0], cubeL[2][0] = tempD[0], tempD[1], tempD[2]
                cubeD[2] = [tempR[2], tempR[1], tempR[0]]
                cubeR[0][2], cubeR[1][2], cubeR[2][2] = tempU[0], tempU[1], tempU[2]
                cubeB[0] = tempB_column3
                cubeB[1] = tempB_column2
                cubeB[2] = tempB_column1

        elif way[0][0] == 'L':
            tempU = [cubeU[0][0], cubeU[1][0], cubeU[2][0]]
            tempB = [cubeB[0][2], cubeB[1][2], cubeB[2][2]]
            tempD = [cubeD[0][0], cubeD[1][0], cubeD[2][0]]
            tempF = [cubeF[0][0], cubeF[1][0], cubeF[2][0]]
            tempL_column1 = [cubeL[0][0], cubeL[1][0], cubeL[2][0]]
            tempL_column2 = [cubeL[0][1], cubeL[1][1], cubeL[2][1]]
            tempL_column3 = [cubeL[0][2], cubeL[1][2], cubeL[2][2]]

            if way[0][1] == '+':
                cubeU[0][0], cubeU[1][0], cubeU[2][0] = tempB[2], tempB[1], tempB[0]
                cubeB[0][2], cubeB[1][2], cubeB[2][2] = tempD[2], tempD[1], tempD[0]
                cubeD[0][0], cubeD[1][0], cubeD[2][0] = tempF
                cubeF[0][0], cubeF[1][0], cubeF[2][0] = tempU
                cubeL[0] = [tempL_column1[2], tempL_column1[1], tempL_column1[0]]
                cubeL[1] = [tempL_column2[2], tempL_column2[1], tempL_column2[0]]
                cubeL[2] = [tempL_column3[2], tempL_column3[1], tempL_column3[0]]
            elif way[0][1] == '-':
                cubeU[0][0], cubeU[1][0], cubeU[2][0] = tempF
                cubeB[0][2], cubeB[1][2], cubeB[2][2] = tempU[2], tempU[1], tempU[0]
                cubeD[0][0], cubeD[1][0], cubeD[2][0] = tempB[2], tempB[1], tempB[0]
                cubeF[0][0], cubeF[1][0], cubeF[2][0] = tempD
                cubeL[0] = tempL_column3
                cubeL[1] = tempL_column2
                cubeL[2] = tempL_column1

        elif way[0][0] == 'R':
            tempU = [cubeU[0][2], cubeU[1][2], cubeU[2][2]]
            tempB = [cubeB[0][0], cubeB[1][0], cubeB[2][0]]
            tempD = [cubeD[0][2], cubeD[1][2], cubeD[2][2]]
            tempF = [cubeF[0][2], cubeF[1][2], cubeF[2][2]]
            tempR_column1 = [cubeR[0][0], cubeR[1][0], cubeR[2][0]]
            tempR_column2 = [cubeR[0][1], cubeR[1][1], cubeR[2][1]]
            tempR_column3 = [cubeR[0][2], cubeR[1][2], cubeR[2][2]]
            if way[0][1] == '+':
                cubeU[0][2], cubeU[1][2], cubeU[2][2] = tempF
                cubeB[0][0], cubeB[1][0], cubeB[2][0] = tempU[2], tempU[1], tempU[0]
                cubeD[0][2], cubeD[1][2], cubeD[2][2] = tempB[2], tempB[1], tempB[0]
                cubeF[0][2], cubeF[1][2], cubeF[2][2] = tempD
                cubeR[0] = [tempR_column1[2], tempR_column1[1], tempR_column1[0]]
                cubeR[1] = [tempR_column2[2], tempR_column2[1], tempR_column2[0]]
                cubeR[2] = [tempR_column3[2], tempR_column3[1], tempR_column3[0]]
            elif way[0][1] == '-':
                cubeU[0][2], cubeU[1][2], cubeU[2][2] = tempB[2], tempB[1], tempB[0]
                cubeB[0][0], cubeB[1][0], cubeB[2][0] = tempD[2], tempD[1], tempD[0]
                cubeD[0][2], cubeD[1][2], cubeD[2][2] = tempF
                cubeF[0][2], cubeF[1][2], cubeF[2][2] = tempU
                cubeR[0] = tempR_column3
                cubeR[1] = tempR_column2
                cubeR[2] = tempR_column1

        way.remove(way[0])

    for i in range(3):
        for j in range(3):
            print(cubeU[i][j], end="")
        print()