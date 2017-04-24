//referenced from https://zh.wikipedia.org/wiki/%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F

#include <iostream>
using namespace std;

class StrategyInterface
{
    public:
        virtual void execute() = 0;
};

class ConcreteStrategyA: public StrategyInterface
{
    public:
        virtual void execute()
        {
            cout << "Called ConcreteStrategyA execute method" << endl;
        }
};

class ConcreteStrategyB: public StrategyInterface
{
    public:
        virtual void execute()
        {
            cout << "Called ConcreteStrategyB execute method" << endl;
        }
};

class ConcreteStrategyC: public StrategyInterface
{
    public:
        virtual void execute()
        {
            cout << "Called ConcreteStrategyC execute method" << endl;
        }
};

class Context
{
    private:
        StrategyInterface *_strategy;

    public:
        Context(StrategyInterface *strategy):_strategy(strategy)
        {
        }

        void set_strategy(StrategyInterface *strategy)
        {
            _strategy = strategy;
        }

        void execute()
        {
            _strategy->execute();
        }
};

int main(int argc, char *argv[])
{
    ConcreteStrategyA concreteStrategyA;
    ConcreteStrategyB concreteStrategyB;
    ConcreteStrategyC concreteStrategyC;

    Context contextA(&concreteStrategyA);
    Context contextB(&concreteStrategyB);
    Context contextC(&concreteStrategyC);

    contextA.execute();
    contextB.execute();
    contextC.execute();
    
    contextA.set_strategy(&concreteStrategyB);
    contextA.execute();
    contextA.set_strategy(&concreteStrategyC);
    contextA.execute();

    return 0;
}
