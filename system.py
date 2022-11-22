class System:
    def __init__(self, rules):
        self.__rules = rules
        self.typeDiseases = {}
        self.distribution()

    def getRules(self):
        return self.__rules

    def saveRule(self, typeDisease, disease, newRule):
        oldRule = self.getResult(newRule, typeDisease)
        if oldRule == 'Робот не определил болезнь':
            self.__rules[f'Rule {len(self.__rules) + 1}'] = {
                f'{typeDisease}': newRule,
                'Заболевание': disease
            }
            return True
        else:
            return False

    def setNewType(self, typeDisease):
        if typeDisease not in self.typeDiseases.keys():
            self.typeDiseases[typeDisease] = []

    def setNewDisease(self, typeDisease, disease):
        if typeDisease in self.typeDiseases.keys():
            if disease not in self.typeDiseases[typeDisease]:
                self.typeDiseases[typeDisease].append(disease)

    def distribution(self):
        for rule in self.__rules:
            typeDisease = list(self.__rules[rule].keys())[0]
            if typeDisease not in self.typeDiseases.keys():
                self.typeDiseases[typeDisease] = []
            if self.__rules[rule]['Заболевание'] not in self.typeDiseases[typeDisease]:
                self.typeDiseases[typeDisease].append(self.__rules[rule]['Заболевание'])

    def getResult(self, userAnswer, typeDisease):
        for rule in self.__rules:
            if self.__checkingRuleForType(rule, typeDisease):
                flag = True
                i = 0
                for symptom in list(list(self.__rules[rule].values())[0].values()):
                    if symptom != list(userAnswer.values())[i]:
                        flag = False
                    i += 1
                if flag:
                    return self.__rules[rule]['Заболевание']
        return "Робот не определил болезнь"

    def getDiseasesByType(self, typeDisease):
        if typeDisease in self.typeDiseases.keys():
            return self.typeDiseases[typeDisease]
        else:
            return []

    def __checkingRuleForType(self, rule, typeDisease):
        return list(self.__rules[rule].keys())[0] == typeDisease
