import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def read_my_csv():
    df = pd.read_csv("data/activities/activity.csv", sep=",")
    selected_columns = ["Duration", "PowerOriginal", "HeartRate"]  
    return df[selected_columns]

def assign_hr_zone(hr, max_hr):
    if hr <= 0.6 * max_hr:
        return 1
    elif hr <= 0.7 * max_hr:
        return 2
    elif hr <= 0.8 * max_hr:
        return 3
    elif hr <= 0.9 * max_hr:
        return 4
    else:
        return 5

def seconds_to_mmss(seconds):
    minutes = seconds // 60
    sec = seconds % 60
    return f"{int(minutes):02d}:{int(sec):02d}"


def make_plot(df, max_hr):
    df_plot = df.head(2000).copy()
    df_plot["Time"] = df_plot.index
    
    # Assign HR zones using max_hr dynamically
    df_plot["HR_Zone"] = df_plot["HeartRate"].apply(lambda hr: assign_hr_zone(hr, max_hr))

    zone_colors = {
        1: "blue",
        2: "green",
        3: "yellow",
        4: "orange",
        5: "red"
    }

    fig = go.Figure()

    # Add Power trace (left y-axis)
    fig.add_trace(go.Scatter(
        x=df_plot["Time"], y=df_plot["PowerOriginal"],
        name="Power", yaxis="y1",
        line=dict(color="purple")
    ))

    # Add Heart Rate traces split by zone (right y-axis)
    for zone in range(1, 6):
        zone_data = df_plot[df_plot["HR_Zone"] == zone]
        fig.add_trace(go.Scatter(
            x=zone_data["Time"], y=zone_data["HeartRate"],
            mode='markers+lines',
            name=f"HR Zone {zone}",
            yaxis="y2",
            marker=dict(color=zone_colors[zone], size=5),
            line=dict(color=zone_colors[zone]),
            hovertemplate='Time: %{x}<br>HR: %{y}<br>Zone: '+str(zone)+'<extra></extra>'
        ))

    fig.update_layout(
        title="Power and Heart Rate (with Zones) over Time",
        xaxis=dict(title="Time"),
        yaxis=dict(title="Power (W)", side="left"),
        yaxis2=dict(title="Heart Rate (bpm)", overlaying="y", side="right"),
        legend=dict(title="Legend")
    )

    return fig, df_plot



if __name__ == "__main__":
    df = read_my_csv()
    pio.renderers.default = "browser"
    fig = make_plot(df)
    fig.show()
    print(df.head(10))