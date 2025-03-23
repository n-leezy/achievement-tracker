FROM node:16-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

# Add a non-root user
RUN addgroup -g 1001 -S appuser && \
    adduser -u 1001 -S appuser -G appuser

# Give proper permissions
RUN mkdir -p node_modules/.cache && chown -R appuser:appuser /app

COPY . .

USER appuser

EXPOSE 3000

CMD ["npm", "start"]