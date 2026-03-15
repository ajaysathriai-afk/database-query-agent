import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class DataVisualizer:

    @staticmethod
    def create_chart(df, chart_type="table"):

        if df is None or df.empty:
            return None

        try:

            numeric_cols = df.select_dtypes(include=['number']).columns

            # BAR
            if chart_type == "bar" and len(numeric_cols) >= 1:
                fig = px.bar(
                    df,
                    x=df.columns[0],
                    y=numeric_cols[0],
                    title="Bar Chart"
                )
                return fig

            # LINE
            elif chart_type == "line" and len(numeric_cols) >= 1:
                fig = px.line(
                    df,
                    x=df.columns[0],
                    y=numeric_cols[0],
                    title="Line Chart"
                )
                return fig

            # PIE
            elif chart_type == "pie" and len(numeric_cols) >= 1:
                fig = px.pie(
                    df,
                    names=df.columns[0],
                    values=numeric_cols[0],
                    title="Pie Chart"
                )
                return fig

            # FALLBACK → TABLE
            fig = go.Figure(data=[go.Table(
                header=dict(
                    values=list(df.columns),
                    fill_color='#6366f1',
                    font=dict(color='white', size=14),
                    align='left'
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    fill_color='#0f172a',
                    font=dict(color='white', size=12),
                    align='left'
                )
            )])

            fig.update_layout(
                title="Query Results",
                margin=dict(l=0, r=0, t=30, b=0)
            )

            return fig

        except Exception as e:
            print(f"Visualization error: {e}")
            return None