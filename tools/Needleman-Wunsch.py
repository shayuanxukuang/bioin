def Needleman(s1,s2,matchscore=5,mismatch=-2,gap=-1):
    m,n=len(s1),len(s2)
    H=[[0]*(n+1)for _ in range(m+1)]
    for i in range(1,m+1):
        H[i][0]=gap*i
    for j in range(1,n+1):
        H[0][j]=gap*j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                score=matchscore
            else:
                score=mismatch

            H[i][j]=max(
                H[i-1][j]+gap,
                H[i][j-1]+gap,
                H[i-1][j-1]+score
            )

    aligment1=[]
    aligment2=[]
    i,j=m,n
    while i>0 and j>0:
        score=H[i][j]
        diag=H[i-1][j-1] if i>0 and j>0 else float('-inf')
        left=H[i][j-1] if j>0 else float('-inf')
        up=H[i-1][j]if i>0 else float('-inf')

        if score==diag+(matchscore if s1[i-1]==s2[j-1] else mismatch):
            aligment1.append(s1[i-1])
            aligment2.append(s2[j-1])
            i-=1
            j-=1

        elif score==left+gap:
            aligment1.append(s1[i-1])
            aligment2.append('-')
            i-=1

        elif score==up+gap:
            aligment1.append('-')
            aligment2.append(s2[j-1])
            j-=1

    aligment1.reverse()
    aligment2.reverse()

    while i>0:
        aligment1.append(s1[i-1])
        aligment2.append('-')
        i-=1
    while j>0:
        aligment1.append('-')
        aligment2.append(s2[j - 1])
        j -= 1

    aligment1=''.join(aligment1)
    aligment2=''.join(aligment2)
    return H[m][n],aligment1,aligment2





def Needleman_affine_pen(s1, s2, matchscore=5, mismatch=-1, gap_open=-3, gap_ex=-1):
    m, n = len(s1), len(s2)
    H = [[0] * (n + 1) for _ in range(m + 1)]
    E = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(1, m + 1):
        H[i][0] = E[i][0] = gap_open + gap_ex * (i - 1)

    for j in range(1, n + 1):
        H[0][j] = E[0][j] = gap_open + gap_ex * (j - 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                score = matchscore
            else:
                score = mismatch

            delete = E[i - 1][j] + gap_ex
            insert = H[i][j - 1] + gap_ex
            mm = H[i - 1][j - 1] + score

            if delete >= insert and delete >= mm:
                H[i][j] = delete
                E[i][j] = E[i - 1][j]
            elif insert >= delete and insert >= mm:
                H[i][j] = insert
                E[i][j] = H[i][j - 1]
            else:
                H[i][j] = mm
                E[i][j] = 0

    alignment1 = ['-'] * m
    alignment2 = ['-'] * n
    pointer1 = m - 1
    pointer2 = n - 1

    # 回溯对齐路径
    while pointer1 >= 0 or pointer2 >= 0:
        if pointer1 == -1:
            alignment2[pointer2] = s2[pointer2]
            pointer2 -= 1
        elif pointer2 == -1:
            alignment1[pointer1] = s1[pointer1]
            pointer1 -= 1
        elif H[pointer1 + 1][pointer2 + 1] == H[pointer1][pointer2 + 1] + gap_ex:
            alignment1[pointer1] = '-'
            pointer1 -= 1
        elif H[pointer1 + 1][pointer2 + 1] == H[pointer1 + 1][pointer2] + gap_ex:
            alignment2[pointer2] = '-'
            pointer2 -= 1
        else:
            alignment1[pointer1] = s1[pointer1]
            alignment2[pointer2] = s2[pointer2]
            pointer1 -= 1
            pointer2 -= 1

    # 反转序列以匹配原始序列的顺序
    alignment1 = ''.join(alignment1)
    alignment2 = ''.join(alignment2)


    return H[m][n], alignment1, alignment2




    return H[m][n], alignment1, alignment2


def Smith_waterman(s1,s2,matchscore=5,mismatch=-2,gap=-1):
    m,n=len(s1),len(s2)
    H=[[float('-inf')]*(n+1)for _ in range(m+1)]
    max_score=float('-inf')
    end_i,end_j=0,0
    for i in range(1,m+1):
        for j in range(1,n+1):
            match=H[i-1][j-1]+(matchscore if s1[i-1]==s2[j-1] else mismatch)
            delete=H[i-1][j]+gap
            insert=H[i][j-1]+gap
            H[i][j]=max(match,delete,insert,0)

            if H[i][j]>max_score:
                max_score=H[i][j]
                end_i,end_j=i,j
    alignment1,alignment2='',''
    i, j = end_i, end_j
    while i > 0 and j > 0:
        # 从最高分数的单元开始回溯
        if H[i][j] == H[i - 1][j - 1] + (matchscore if s1[i - 1] == s2[j - 1] else mismatch):
            alignment1 = s1[i - 1] + alignment1
            alignment2 = s2[j - 1] + alignment2
            i -= 1
            j -= 1
        elif H[i][j] == H[i - 1][j] + gap:
            alignment1 = '-' + alignment1
            i -= 1
        elif H[i][j] == H[i][j - 1] + gap:
            alignment2 = '-' + alignment2
            j -= 1
        else:
            # 如果当前分数是0，说明这里没有对齐，可能是因为序列的开始
            if H[i][j] == 0:
                break
            else:

                break



    return max_score, alignment1, alignment2


def Smith_waterman_affine(s1, s2, matchscore=3, mismatch=-2, gap_open=-3, gap_extend=-1):
    m, n = len(s1), len(s2)
    H = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

    max_score = float('-inf')
    end_i, end_j = 0, 0

    # 初始化第一行和第一列
    for i in range(1, m + 1):
        H[i][0] = H[i - 1][0] + gap_extend if i > 1 else 0
    for j in range(1, n + 1):
        H[0][j] = H[0][j - 1] + gap_extend if j > 1 else 0

        # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = H[i - 1][j - 1] + (matchscore if s1[i - 1] == s2[j - 1] else mismatch)
            delete = H[i - 1][j] + gap_extend
            if i > 1 and H[i - 1][j] != float('-inf'):
                delete = max(delete, H[i - 2][j] + gap_open)
            H[i][j] = max(0, match, delete)
            if H[i][j] > max_score:
                max_score = H[i][j]
                end_i, end_j = i, j

                # 回溯构建对齐
    alignment1, alignment2 = '', ''
    i, j = end_i, end_j
    while i > 0 and j > 0:
        score_current = H[i][j]
        score_diag = H[i - 1][j - 1]
        score_above = H[i - 1][j]

        if score_current == score_diag + (matchscore if s1[i - 1] == s2[j - 1] else mismatch):
            alignment1 = s1[i - 1] + alignment1
            alignment2 = s2[j - 1] + alignment2
            i -= 1
            j -= 1
        elif score_current == score_above + gap_extend or (i > 1 and score_current == H[i - 2][j] + gap_open):
            # s1中有删除或gap_open，s2中无变化
            alignment1 = s1[i - 1] + alignment1  # 注意：这里通常不会添加s1的字符，但保持以符合原始逻辑
            alignment2 = '-' + alignment2
            i -= 1
        else:
            # 隐含的s2中的插入
            alignment1 = '-' + alignment1
            alignment2 = s2[j - 1] + alignment2
            j -= 1

            # 处理s1末尾的间隙
    while i > 0:
        alignment1 = '-' + alignment1
        i -= 1

    return max_score, alignment1, alignment2
s1 = "CATCAAATACGGCATCAAATCCAGATTTCTCGTCGTCGACGAAGTCTTCAGCATCCCACCCCACCTGTTG"
s2 = "CTACAGGCTCCCACAAGACATCACCAGGTACCTGCCCAGCGCGATTACCCGGGCAATCCAGAAATTTC"
score, align1, align2 = Smith_waterman_affine(s1,s2)
print(f"Score: {score}, Alignment 1: {align1}, Alignment 2: {align2}")

