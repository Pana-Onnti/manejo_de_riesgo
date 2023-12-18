import quantstats as qs
import pandas as pd
import io
import sys


def get_last_two_values(row):
    values = row.dropna().values[-2:]
    return pd.Series(values, index=[0, 1])


class PortfolioItem:
    StartPeriod = "StartPeriod"
    EndPeriod = "EndPeriod"
    RiskFreeRate = "RiskFreeRate"
    TimeInMarket = "TimeInMarket"
    CumulativeReturn = "CumulativeReturn"
    CAGRPercentage = "CAGRPercentage"
    Sharpe = "Sharpe"
    ProbSharpeRatio = "ProbSharpeRatio"
    Sortino = "Sortino"
    SortinoSquareRoot2 = "SortinoSquareRoot2"
    Omega = "Omega"
    MaxDrawdown = "MaxDrawdown"
    LongestDDDays = "LongestDDDays"
    GainPainRatio = "GainPainRatio"
    GainPain1M = "GainPain1M"
    PayoffRatio = "PayoffRatio"
    ProfitFactor = "ProfitFactor"
    CommonSenseRatio = "CommonSenseRatio"
    CPCIndex = "CPCIndex"
    TailRatio = "TailRatio"
    OutlierWinRatio = "OutlierWinRatio"
    OutlierLossRatio = "OutlierLossRatio"
    MTD = "MTD"
    r3M = "r3M"
    r6M = "r6M"
    YTD = "YTD"
    r1Y = "r1Y"
    r3Yann = "r3Yann"
    r5Yann = "r5Yann"
    r10Yann = "r10Yann"
    Alltimeann = "Alltimeann"
    AvgDrawdown = "AvgDrawdown"
    AvgDrawdownDays = "AvgDrawdownDays"
    RecoveryFactor = "RecoveryFactor"
    Ulcer_Index = "Ulcer_Index"
    Serenity_Index = "Serenity_Index"

# Crear una lista de propiedades sin los tipados
propiedades = [attr for attr in dir(PortfolioItem) if not callable(getattr(PortfolioItem, attr)) and not attr.startswith("__")]

indicators_list = propiedades

def generate_report(daily_returns):
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    qs.reports.metrics(daily_returns, benchmark='SPY')

    sys.stdout = sys.__stdout__
    metrics_output = output_buffer.getvalue()

    try:
        df = pd.read_csv(io.StringIO(metrics_output), delim_whitespace=True)
    except pd.errors.EmptyDataError:
        df = None
        print("Empty")
    except pd.errors.ParserError:
        print("ParserError")
        df = None

    if df is not None:
        result = df.apply(get_last_two_values, axis=1)

        list_indicators = pd.DataFrame(indicators_list)

        df_r = result.drop([0, 1])
        df_r = df_r.reset_index(drop=True)

        report_df = pd.concat([list_indicators, df_r], axis=1)
        report_df.columns = ['Indicator', 'SPY', 'Portfolio']
        report_df = report_df.reset_index(drop=True)
        report_df = report_df.set_index('Indicator')
        return report_df
