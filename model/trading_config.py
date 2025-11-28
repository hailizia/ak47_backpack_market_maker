#!/usr/bin/env python

from dataclasses import dataclass


@dataclass
class TradingConfig:
    """Configuration class for trading parameters."""
    ticker: str
    market_type: str
    public_key: str
    secret_key: str

