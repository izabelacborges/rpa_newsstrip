from datetime import datetime as dt


def get_start_date(today, months):
    if months <= 1:
        return today.replace(day=1)
    
    current_month = today.month
    start_month = current_month - (months - 1)
    return today.replace(day=1, month=start_month)


def get_date_range(timespan):
    now = dt.now()
    end_date = now.strftime("%m/%d/%Y")

    then = get_start_date(now, timespan)
    start_date = then.strftime("%m/%d/%Y")

    return start_date, end_date


def get_number_from_sentence(sentence):
    numbers_list = re.findall(r'[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', sentence)
    return [int(s.replace(',','')) for s in numbers_list]
