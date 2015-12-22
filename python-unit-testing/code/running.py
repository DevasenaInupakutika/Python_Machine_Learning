def running(values):
    
    assert len(values)>0
    result = [values[0]]
    for v in values[1:]:
        assert result[-1] >= 0
        result.append(result[-1] + v)
    assert result[-1] >= result[0]
    return result

