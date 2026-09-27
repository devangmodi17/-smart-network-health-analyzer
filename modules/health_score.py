def calculate_health_score(latency, packet_loss):
    if latency < 50:
        latency_score = 100
    elif latency < 100:
        latency_score = 80
    elif latency < 200:
        latency_score = 60
    else:
        latency_score = 30

    if packet_loss == 0:
        loss_score = 100
    elif packet_loss <= 2:
        loss_score = 80
    elif packet_loss <= 5:
        loss_score = 60
    else:
        loss_score = 30

    health_score = (latency_score * 0.6) + (loss_score * 0.4)

    return health_score

def get_health_status(health_score):
    if health_score >= 80:
        return "Healthy"
    elif health_score >= 60:
        return "Moderate"
    elif health_score >= 40:
        return "Poor"
    else:
        return "Critical"
