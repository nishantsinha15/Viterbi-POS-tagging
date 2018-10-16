class Reader:

    def __init__(self):
        with open("Training set_HMM.txt") as f:
            self.data = f.readlines()

    def transition_probability(self):
        tags1 = []
        for i in range(len(self.data)):
            temp = self.data[i].split()
            if len(temp) == 2:
                tags1.append(temp[1])
            else:
                tags1.append('END')
        tags = []
        for i in range(len(tags1)-1):
            if tags1[i+1] != 'END':
                tags.append(tags1[i])
        tags.append('END')
        tags1 = set(tags)
        p_trans = {}
        count = {}
        for i in tags1:
            count[i] = 0
            p_trans[i] = {}
            for j in tags1:
                p_trans[i][j] = 0
        for i in range(len(tags)-1):
            p_trans[tags[i]][tags[i+1]] += 1
            count[tags[i]] += 1
        for k1 in p_trans:
            for k2 in p_trans[k1]:
                p_trans[k1][k2] = (p_trans[k1][k2] + 1)/(count[k1] + len(tags1) - 1)

        return p_trans

    def emission_probability(self):
        count = {}
        count_term = {}
        for i in range(len(self.data)):
            temp = self.data[i].split()
            if len(temp) == 2:
                if temp[1] not in count:
                    count[temp[1]] = 0
                count[temp[1]] += 1
                if (temp[0], temp[1]) not in count_term:
                    count_term[(temp[0], temp[1])] = 0
                count_term[(temp[0], temp[1])] += 1
        for i in count_term:
            count_term[i] /= count[i[1]]
        return count_term


class Viterbi:

    def __init__(self):
        r = Reader()
        self.p_trans = r.transition_probability()
        self.p_emission = r.emission_probability()

