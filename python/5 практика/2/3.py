import coverage

cov = coverage.Coverage()
cov.start()

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def main():
    assert distance(0, 0, 3, 4) == 5.0

if __name__ == "__main__":
    main()

cov.stop()
cov.save()
cov.html_report(directory='D:\\code\\_4\\python\\5 практика\\2')