def read_urls_from_csv(file_path):
    """ 
    Returns URLs as a list.
    
    Args:
    - file_path (str)
    
    Returns:
    - A list of URLs
    """
    df = pd.read_csv(file_path, header=None, usecols=[0])
    urls = df[0].dropna().unique().tolist()
    return urls


def capture_network_activity():
    print("Capturing network activity...")
    time.sleep(1)
    data = {
        'timestamp': pd.date_range(start='2025-01-20', periods=100, freq='H'),
        'request_count': np.random.randint(1, 100, 100)
    }
    df = pd.DataFrame(data)
    print("Data captured.")
    return df
