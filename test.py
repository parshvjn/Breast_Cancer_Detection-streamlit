
def columnFixer(df, setCols):
    for i, col in enumerate(df.columns):
        if '_se' in col:
            # print(col[:-3])
            splited1 = col.split('_')
            result = " ".join(splited1)
            df = df.rename(columns={col:f'{result[:-3]} error'})
        elif 'mean' in col or 'worst' in col:
            splited2 = col.split('_')
            last = splited2.pop()
            splited2.insert(0, last)
            result = " ".join(splited2)
            df = df.rename(columns = {col:result})

    # print(df.columns)
    df = df[setCols] #rearranging
    return df