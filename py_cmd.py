import click
import pandas as pd


def check(filename):
    df = pd.read_csv(filename)
    if df is None:
        click.echo("no dataset is loaded")
    return df


@click.group()
def cli():
    pass


@click.command(name="load_data")
@click.argument("filename", type=click.Path(exists=True), default="tv_shows.csv")
@click.option("-hd", "--head", default=-1, help="Show head n line")
@click.option("-tl", "--tail", default=-1, help="show tail n line")
def load_data(filename, head, tail):
    """Load data from existed csv file."""
    df = check(filename)
    if head > 0 or tail < 0:
        head = 5 if head <= 0 else head
        print(df.head(head))
    elif tail > 0:
        print(df.tail(tail))


@click.command(name="sort")
@click.argument("cols")
@click.argument("filename", type=click.Path(exists=True), default="tv_shows.csv")
@click.option("-n", "--num", default=0, help='number of line to show')
@click.option("-as/-des", "--ascending/--descending", default=False)
def sort(cols, num, ascending, filename):
    """Sort data from cols with separator `,`."""
    df = check(filename)
    cols = [key.strip() for key in cols.split(",")]
    res = df.sort_values(cols, ascending=ascending)
    if num > 0:
        res = res.iloc[:num]
    print(res)


@click.command()
@click.argument("col_name")
@click.argument("filename", type=click.Path(exists=True), default="tv_shows.csv")
@click.option("-n", "--num", default=0, help='number of line to show')
@click.option("-as/-des", "--ascending/--descending", default=False)
def count(col_name, num, ascending, filename):
    """Goup data with column name."""
    df = check(filename)
    g = df.groupby(col_name)
    res = g.size()
    if ascending:
        res = res[::-1]
    if num > 0:
        res = res.iloc[:num]
    print(res)


@click.command(name="to_type")
@click.option("-t", "--type", default="csv", help='new type of file')
@click.argument("filename", type=click.Path(exists=True), default="tv_shows.csv")
def change_type(tp, filename):
    """Transfer csv file to pkl or gdf file."""
    name = filename.split(".")[0] + "." + tp
    df = check(filename)
    if tp == "pkl":
        df.to_pickle(name)
    elif tp == "gdf":
        df.to_hdf(name, "df")
    elif tp == "csv":
        df.to_csv(name)
    else:
        click.echo("unknow type: " + tp)


cli.add_command(load_data)
cli.add_command(sort)
cli.add_command(count)
cli.add_command(change_type)

if __name__ == "__main__":
    cli()
