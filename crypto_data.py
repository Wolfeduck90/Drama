"""
CryptoVisor - Cryptocurrency Data Module
========================================

This module contains the cryptocurrency database and data management functions.
It provides predefined crypto data with metrics for investment analysis.

Author: CryptoVisor Development Team
"""

# Predefined cryptocurrency database with investment metrics
# Each crypto has profitability and sustainability indicators
crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",           # Current price movement
        "market_cap": "high",              # Market capitalization tier
        "energy_use": "high",              # Energy consumption level
        "sustainability_score": 3,         # Sustainability rating (1-10)
        "volatility": "high",              # Price volatility level
        "adoption": "very_high",           # Mainstream adoption level
        "description": "The original cryptocurrency with highest market cap but environmental concerns"
    },
    
    "Ethereum": {
        "symbol": "ETH",
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",            # Improved after Ethereum 2.0
        "sustainability_score": 6,
        "volatility": "medium",
        "adoption": "high",
        "description": "Smart contract platform with good balance of growth and sustainability"
    },
    
    "Cardano": {
        "symbol": "ADA",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",               # Proof-of-Stake consensus
        "sustainability_score": 8,
        "volatility": "medium",
        "adoption": "medium",
        "description": "Eco-friendly blockchain focused on sustainability and academic research"
    },
    
    "Solana": {
        "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "volatility": "high",
        "adoption": "medium",
        "description": "Fast and efficient blockchain with growing DeFi ecosystem"
    },
    
    "Polkadot": {
        "symbol": "DOT",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "volatility": "medium",
        "adoption": "low",
        "description": "Interoperable blockchain network enabling cross-chain transfers"
    }
}

def get_crypto_data(crypto_name):
    """
    Retrieve data for a specific cryptocurrency.
    
    Args:
        crypto_name (str): Name of the cryptocurrency
        
    Returns:
        dict: Cryptocurrency data or None if not found
    """
    # Case-insensitive search for crypto name
    for name, data in crypto_db.items():
        if name.lower() == crypto_name.lower():
            return {name: data}
    return None

def get_all_cryptos():
    """
    Get all available cryptocurrencies.
    
    Returns:
        dict: Complete cryptocurrency database
    """
    return crypto_db

def find_cryptos_by_criteria(criteria):
    """
    Find cryptocurrencies matching specific criteria.
    
    Args:
        criteria (dict): Dictionary of criteria to match
        
    Returns:
        dict: Matching cryptocurrencies
    """
    matching_cryptos = {}
    
    for name, data in crypto_db.items():
        match = True
        
        # Check each criterion
        for key, value in criteria.items():
            if key in data and data[key] != value:
                match = False
                break
        
        if match:
            matching_cryptos[name] = data
    
    return matching_cryptos

def get_top_sustainable_cryptos(min_score=7):
    """
    Get cryptocurrencies with high sustainability scores.
    
    Args:
        min_score (int): Minimum sustainability score (1-10)
        
    Returns:
        dict: Sustainable cryptocurrencies sorted by score
    """
    sustainable_cryptos = {}
    
    for name, data in crypto_db.items():
        if data["sustainability_score"] >= min_score:
            sustainable_cryptos[name] = data
    
    # Sort by sustainability score (descending)
    sorted_cryptos = dict(sorted(
        sustainable_cryptos.items(),
        key=lambda x: x[1]["sustainability_score"],
        reverse=True
    ))
    
    return sorted_cryptos

def get_profitable_cryptos():
    """
    Get cryptocurrencies with rising price trends and high market cap.
    
    Returns:
        dict: Potentially profitable cryptocurrencies
    """
    profitable_cryptos = {}
    
    for name, data in crypto_db.items():
        # Define profitability criteria
        if (data["price_trend"] == "rising" and 
            data["market_cap"] in ["high", "medium"]):
            profitable_cryptos[name] = data
    
    return profitable_cryptos

def get_balanced_investments():
    """
    Get cryptocurrencies with good balance of profitability and sustainability.
    
    Returns:
        dict: Balanced investment options
    """
    balanced_cryptos = {}
    
    for name, data in crypto_db.items():
        # Balance criteria: rising/stable trend + sustainability score >= 6
        if ((data["price_trend"] in ["rising", "stable"]) and 
            data["sustainability_score"] >= 6):
            balanced_cryptos[name] = data
    
    return balanced_cryptos

# Market insights and analysis functions
def analyze_market_trends():
    """
    Analyze overall market trends from available data.
    
    Returns:
        dict: Market analysis summary
    """
    rising_count = 0
    stable_count = 0
    falling_count = 0
    avg_sustainability = 0
    
    total_cryptos = len(crypto_db)
    
    for data in crypto_db.values():
        if data["price_trend"] == "rising":
            rising_count += 1
        elif data["price_trend"] == "stable":
            stable_count += 1
        else:
            falling_count += 1
        
        avg_sustainability += data["sustainability_score"]
    
    avg_sustainability = avg_sustainability / total_cryptos
    
    return {
        "total_cryptos": total_cryptos,
        "rising_trends": rising_count,
        "stable_trends": stable_count,
        "falling_trends": falling_count,
        "average_sustainability": round(avg_sustainability, 2),
        "market_sentiment": "bullish" if rising_count > stable_count else "neutral"
    }
