def pick_forwards(df):
    """
    :param df: the total df of the week
    :return: the top 3 forward's name and points
    """
    df = df[df['position']=='FWD']
    return df.nlargest(3, ['total_points'])


def pick_midfielders(df):
    """
    :param df: the total df of the week
    :return: the top 6 midfielders name and points
    """
    df = df[df['position']=='MID']
    return df.nlargest(6, ['total_points'])


def pick_defenders(df):
    """
    :param df: the total df of the week
    :return: the top 6 defenders name and points
    """
    df = df[df['position'] == 'DEF']
    return df.nlargest(6, ['total_points'])


def pick_keepers(df):
    """
    :param df: the total df of the week
    :return: the top 2 keepers name and points
    """
    df = df[df['position']=='GK']
    return df.nlargest(2, ['total_points'])