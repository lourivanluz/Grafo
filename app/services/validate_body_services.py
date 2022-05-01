def verification_graphSechma(data:dict):
    dataTest = data.get('data')
    if dataTest:
        if isinstance(dataTest,list):
            element = dataTest[0]
            if isinstance(element,dict):
                for index,elmentTest in enumerate(dataTest):
                    source = elmentTest.get("source")
                    target = elmentTest.get("target")
                    distance = elmentTest.get("distance")
                    if not source or not target or not distance:
                        return f"not heve source or target or distance in {index+1}º element"
                return "valid filds"
            else:
                return "element in list not is dict"
        else:
            return "data not is list"
    else:
        return "no have field 'data'"