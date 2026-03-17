import plotly.express as px


def instruction_mix_chart(df):
    """
    Pie chart for instruction mix
    """
    mix = df["category"].value_counts().reset_index()
    mix.columns = ["category", "count"]

    fig = px.pie(
        mix,
        values="count",
        names="category",
        title="Instruction Mix Distribution"
    )

    return fig


def cycle_loss_chart(penalties):
    """
    Bar chart showing cycle loss sources
    """

    labels = list(penalties.keys())
    values = list(penalties.values())

    fig = px.bar(
        x=labels,
        y=values,
        title="Cycle Loss Breakdown",
        labels={"x": "Hazard Type", "y": "Cycle Penalty"}
    )

    return fig